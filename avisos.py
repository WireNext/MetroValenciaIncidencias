import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.metrovalencia.es/es/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar el div con la clase y id indicados
contenedor_avisos = soup.find('div', {
    'class': 'col-6 feed-main-avisos js-resultado-alertas',
    'role': 'region',
    'id': 'i4t-news-alert',
    'aria-label': 'Avisos de accesibilidad.'
})

if contenedor_avisos:
    avisos = []
    # Suponiendo que cada aviso está dentro de un div o elemento con clase 'avisos__item' o similar
    for aviso in contenedor_avisos.find_all('div', class_='avisos__item'):
        titulo = aviso.find('h4')
        descripcion = aviso.find('p')
        avisos.append({
            'titulo': titulo.text.strip() if titulo else 'Sin título',
            'descripcion': descripcion.text.strip() if descripcion else 'Sin descripción'
        })

    # Guardar en JSON
    with open('avisos_servicio.json', 'w', encoding='utf-8') as f:
        json.dump(avisos, f, ensure_ascii=False, indent=2)

    print(f"{len(avisos)} avisos encontrados y guardados en 'avisos_servicio.json'")
else:
    print("No se encontró el contenedor de avisos en la página.")
