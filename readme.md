# AI Pipeline Project

## Project Overview
This project implements a Flask-based server that processes images through a YOLOv5 object detector, ResNet50 for classification and a Transformer-based captioning model. It contains an AI pipeline application that operates as a service, which receives a simple API request with a list of image URLs and returns a detailed JSON response.

## Setup and Running

### Requirements
- Python 3.8+
- pip packages as specified in `requirements.txt`

### Installation
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt

### Run the Flask application:
2. Install Python dependencies:
   ```bash
    python app.py       

### Usage

Send a POST request to http://localhost:5000/process with a JSON payload with image URLs:    
{
  "Images": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
}

You can also add links of the images to image_input.py to send images through the pipeline. Run the following command
   ```bash
   python image_input.py
   ```

### Output

The server returns a JSON response with detection results and captions for each image. It also returns annotated images with detection boxes, class labels and image caption.
