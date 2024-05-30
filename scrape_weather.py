import requests
from bs4 import BeautifulSoup
import json

# URL de la page à scraper
url = "https://www.meteociel.fr/previsions/1581/castellane.htm"

# Envoyer une requête pour obtenir le contenu de la page
response = requests.get(url)
response.encoding = 'iso-8859-1'  # Spécifier l'encodage si nécessaire

# Parser le contenu HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Trouver la table contenant les prévisions météorologiques
table = soup.find('table', {'style': 'border-collapse: collapse;'})

# Extraire les données météorologiques
data = []
for row in table.find_all('tr')[2:]:  # Skipping header rows
    cols = row.find_all('td')
    if len(cols) > 10:  # Pour s'assurer que la ligne contient des données météorologiques
        day = cols[0].text.strip()
        time = cols[1].text.strip()
        temp = cols[2].text.strip().split(' ')[0]
        wind_direction = cols[4].find('img')['title']
        wind_speed = cols[5].text.strip()
        wind_gust = cols[6].text.strip()
        rain = cols[7].text.strip()
        humidity = cols[8].text.strip()
        pressure = cols[9].text.strip()
        weather = cols[10].find('img')['title']

        data.append({
            'day': day,
            'time': time,
            'temperature': temp,
            'wind_direction': wind_direction,
            'wind_speed': wind_speed,
            'wind_gust': wind_gust,
            'rain': rain,
            'humidity': humidity,
            'pressure': pressure,
            'weather': weather
        })

# Écrire les données dans un fichier JSON
with open('meteo_castellane.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Les données météo ont été enregistrées dans 'meteo_castellane.json'")
