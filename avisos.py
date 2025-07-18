import requests
from bs4 import BeautifulSoup
import json

url = "https://www.metrovalencia.es/wp-content/themes/metrovalencia/functions/ajax-no-wp.php"

payload = {
    "action": "formularios_ajax",
    "data": "action=comprobar-usuario&lang=es"
}

try:
    response = requests.post(url, data=payload)
    response.raise_for_status()
    json_data = response.json()
    html_alertas = json_data.get("htmlAlertas", "")

    soup = BeautifulSoup(html_alertas, "html.parser")

    avisos = []

    for alerta in soup.select(".feed-noticias.alerta-general"):
        lineas = alerta.select(".linea img")
        lineas_texto = [img['alt'] for img in lineas]
        texto_alerta = alerta.select_one(".noticia-min span").get_text(strip=True)
        avisos.append({
            "lineas_afectadas": lineas_texto,
            "texto_alerta": texto_alerta
        })

    # Guardar en JSON
    with open("avisos_metrovalencia.json", "w", encoding="utf-8") as f:
        json.dump(avisos, f, ensure_ascii=False, indent=4)

    print(f"{len(avisos)} avisos guardados en avisos_metrovalencia.json")

except Exception as e:
    print("Error al obtener o procesar los avisos:", e)
