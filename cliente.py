import requests
import json

url = "http://127.0.0.1:5000/productos"

payload = json.dumps({
    "nombre": "Laptop Lenovo",
    "precio": 850.00,
    "stock": 10
})

headers = {
    "Content-Type": "application/json"
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)