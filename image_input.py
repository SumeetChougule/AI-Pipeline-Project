import requests

url = "http://127.0.0.1:5000/process"
headers = {"Content-Type": "application/json"}

data = {
    "Images": [
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-0.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-1.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-10.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-11.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-12.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-13.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-14.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-15.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-18.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-19.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-2.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-20.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-21.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-22.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-23.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-24.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-25.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-26.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-3.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-4.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-5.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-7.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-8.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-9.jpg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-16.jpeg",
        "https://raw.githubusercontent.com/SumeetChougule/image-hosting/main/images/image-17.jpeg",
    ]
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
