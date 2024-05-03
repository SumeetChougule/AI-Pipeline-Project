import json
import torch
import requests
from io import BytesIO
from transformers import pipeline
from torchvision import transforms
from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont
from torchvision.models import resnet50, ResNet50_Weights


# Initialize Flask app
app = Flask(__name__)

# Load YOLO model
model_yolo = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

# Load classification model and weights
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()

# Load image-captioning model
image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")


def classify_objects(url, detections):
    """
    Classify detected objects using ResNet50.
    """
    preprocess = weights.transforms()

    classifications = []
    for det in detections:
        # For each detection, crop the object and classify it
        crop = Image.open(requests.get(url, stream=True).raw)
        crop = crop.crop((det["xmin"], det["ymin"], det["xmax"], det["ymax"]))
        crop = preprocess(crop).unsqueeze(0)  # Add batch dimension

        with torch.no_grad():
            prediction = model(crop).squeeze(0).softmax(0)
            class_id = prediction.argmax().item()
            score = prediction[class_id].item()

        # Retrieve the human-readable class name from the model's metadata
        category_name = weights.meta["categories"][class_id]

        classifications.append(
            {
                "object": det["name"],
                "class_id": class_id,
                "class_label": category_name,
                "score": f"{100 * score:.1f}%",
            }
        )

    return classifications


def generate_caption(image_url):
    """
    Generate a caption for the image
    """
    result = image_to_text(image_url)
    caption = result[0]["generated_text"]
    return caption


# Caption font to add to an image
def get_font(size):
    response = requests.get(
        "https://sumeetchougule.github.io/image-hosting/Roboto-Regular.ttf"
    )
    font_bytes = BytesIO(response.content)
    return ImageFont.truetype(font_bytes, size)


font = get_font(40)


# Endpoint for processing images
@app.route("/process", methods=["POST"])
def process_images():
    data = request.get_json()
    image_urls = data.get("Images", [])
    results = []

    for url in image_urls:
        try:
            # Perform detection directly using the image URL
            results_yolo = model_yolo(url)
            detections = results_yolo.pandas().xyxy[0].to_dict(orient="records")

            # Classify detected objects
            classifications = classify_objects(url, detections)

            # Image-caption
            caption = generate_caption(url)

            results.append(
                {
                    "url": url,
                    "detection_results": detections,
                    "classification_results": classifications,
                    "caption": caption,
                }
            )

            # Extract the image with detections drawn on it
            detected_image = results_yolo.render()[0]
            pil_detected_image = Image.fromarray(
                detected_image
            )  # Convert to PIL Image for further processing

            # Append caption to image (load the saved image and add caption text)
            # Path to the saved image with detections
            image_name = results_yolo.files[0]
            image_editable = ImageDraw.Draw(pil_detected_image)
            image_editable.text((10, 10), caption, font=font, fill="white")
            pil_detected_image.save(image_name)  # Save the image with the caption

        except Exception as e:
            results.append({"url": url, "error": str(e)})

        # Save results to a JSON file
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
