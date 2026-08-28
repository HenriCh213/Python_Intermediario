import json
import os



with open('key.json', "r", encoding="utf-8") as f:
    dados = json.load(f)
        
api_key = dados.get("API_KEY")

API_KEY = api_key
