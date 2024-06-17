import requests

data = {
    "year": "2023",
    "month": "05",
}

url = "http://localhost:9696/predict"
response = requests.post(url, json=data)
print(response.json())
