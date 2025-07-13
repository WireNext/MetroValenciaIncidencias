import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.metrovalencia.es/es/avisos-e-incidencias/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

estacions = soup.find_all('div', class_='avisos__item')

avisos = []

for estacio in estacions:
    nom = estacio.find('h4').text.strip()
    descripcio = estacio.find('p').text.strip()
    avisos.append({
        'estacio': nom,
        'descripcio': descripcio
    })

# Convertir a JSON y mostrar por consola o guardar en archivo
json_output = json.dumps(avisos, ensure_ascii=False, indent=2)
print(json_output)

# Opcional: guardar en archivo para luego servir desde tu web
with open('avisos_metrovalencia.json', 'w', encoding='utf-8') as f:
    f.write(json_output)
