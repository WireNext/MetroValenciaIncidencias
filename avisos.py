import requests

url = 'https://www.metrovalencia.es/es/'
response = requests.get(url)

# Imprime los primeros 1000 caracteres para no saturar la consola
print(response.text[:1000])
