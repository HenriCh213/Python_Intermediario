import requests
import matplotlib.pyplot as plt
from skimage import io
from Q1 import API_KEY
from Q4 import max_sol

rover_name = "curiosity"
url_photos = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

sol_alvo = max_sol 

CAMERAS_ALVO = {"NAVCAM", "FHAZ", "RHAZ"}

print(f"🔍 Buscando fotos do Rover {rover_name.capitalize()} para o Sol {sol_alvo}...")
print(f"📷 Câmeras selecionadas: {', '.join(CAMERAS_ALVO)}\n")

pagina = 1
total_fotos_plotadas = 0

while True:
    params_photos = {
        "api_key": API_KEY,
        "sol": sol_alvo,
        "page": pagina
    }
    
    response = requests.get(url_photos, params=params_photos)
    
    if response.status_code != 200:
        print(f"⚠️ Erro ao buscar página {pagina}: Status {response.status_code}")
        break
        
    dados = response.json()
    lista_fotos = dados.get("photos")
    
    if not lista_fotos:
        print(f"🛑 Fim da paginação. Nenhuma foto encontrada na página {pagina}.")
        break
        
    print(f"📄 Processando Página {pagina} ({len(lista_fotos)} fotos encontradas no lote)...")
    
    for foto in lista_fotos:
        camera_info = foto.get("camera", {})
        cam_nome = camera_info.get("name")
        foto_id = foto.get("id")
        img_src = foto.get("img_src")
        
        if cam_nome in CAMERAS_ALVO:
            try:
                if img_src.startswith("http://"):
                    img_src = img_src.replace("http://", "https://", 1)
                
                img_matriz = io.imread(img_src)
                
                plt.figure(figsize=(7, 7))
                
                if len(img_matriz.shape) == 2:
                    plt.imshow(img_matriz, cmap="gray")
                else:
                    plt.imshow(img_matriz)
                
                titulo = f"Página: {pagina} | Câmera: {cam_nome} | ID: {foto_id}"
                plt.title(titulo, fontsize=12, fontweight="bold")
                plt.axis("off")
                plt.tight_layout()
                plt.show()
                
                total_fotos_plotadas += 1
                
            except Exception as e:
                print(f"⚠️ Não foi possível carregar a foto ID {foto_id}: {e}")
                
    pagina += 1

print(f"\n✨ Processamento finalizado! Total de {total_fotos_plotadas} fotos exibidas.")