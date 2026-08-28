import requests
import matplotlib.pyplot as plt
from skimage import io
from Q1 import API_KEY

url_base = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": API_KEY
}

response = requests.get(url_base, params=params)

headers = response.headers

rate_limit = headers.get("X-RateLimit-Limit")
rate_remaining = headers.get("X-RateLimit-Remaining")

print("INFORMAÇÕES DE RATE LIMIT:")
print(f"• X-RateLimit-Limit (Limite Total): {rate_limit} requisições/hora")
print(f"• X-RateLimit-Remaining (Restante): {rate_remaining} requisições disponíveis")