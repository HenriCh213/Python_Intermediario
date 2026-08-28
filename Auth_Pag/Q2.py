import requests
import matplotlib.pyplot as plt
from skimage import io
from Auth_Pag.Q1 import API_KEY

url_base = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": API_KEY
}

response = requests.get(url_base, params=params)

if response.status_code == 200:
    dados_apod = response.json()
    
    media_type = dados_apod.get("media_type")
    
    if media_type == "image":

        img_url = dados_apod.get("hdurl") or dados_apod.get("url")
        

        img = io.imread(img_url)
        
        plt.figure(figsize=(10, 7))
        plt.imshow(img)
        plt.title(dados_apod.get("title", "APOD"), fontsize=14, fontweight="bold")
        plt.axis("off")
        plt.tight_layout()
        plt.show()
    else:
        print(f"Não foi possível carregar!!!.")

else:
    print(f" Erro na requisição: Status Code {response.status_code}")
