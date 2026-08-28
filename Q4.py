import requests
from Q1 import API_KEY

url_manifest = f"https://api.nasa.gov/mars-photos/api/v1/manifests/curiosity"

params_manifest = {
    "api_key": API_KEY
}

response_manifest = requests.get(url_manifest, params=params_manifest)

if response_manifest.status_code == 200:
    dados_manifest = response_manifest.json()
    photo_manifest = dados_manifest.get("photo_manifest", {})
    
    max_sol = photo_manifest.get("max_sol")
    max_date = photo_manifest.get("max_date")
    total_photos = photo_manifest.get("total_photos")
    status = photo_manifest.get("status")
    
    print("=" * 60)
    print(f"🤖 RELATÓRIO DO ROVER: {photo_manifest.get('name').upper()}")
    print("=" * 60)
    print(f"• Status da Missão: {status}")
    print(f"• Max Sol (Último dia marciano de fotos): {max_sol}")
    print(f"• Max Date (Última data terrestre): {max_date}")
    print(f"• Total de fotos acumuladas: {total_photos}")
    print("=" * 60)
else:
    print(f"❌ Erro ao acessar manifesto: {response_manifest.status_code}")
    print(response_manifest.text)