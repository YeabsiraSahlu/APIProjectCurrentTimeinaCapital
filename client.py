import requests
import os


API_URL = "http://34.123.41.232:5000/api/time?city=London"
API_TOKEN = os.getenv("API_TOKEN", "default-token")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)
