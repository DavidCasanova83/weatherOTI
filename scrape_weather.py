import requests
from bs4 import BeautifulSoup
import json

def scrape_weather_data(url):
    response = requests.get(url)
    response.encoding = 'iso-8859-1'  # Spécifier l'encodage si nécessaire
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Trouver la table contenant les prévisions météorologiques
    table = soup.find('table', {'style': 'border-collapse: collapse;'})
    
    # Extraire les données météorologiques
    data = []  # Créer une liste vide pour stocker les données météorologiques
    for row in table.find_all('tr')[2:]:  # Parcourir chaque ligne de la table à partir de la troisième ligne (en sautant les lignes d'en-tête)
      cols = row.find_all('td')  # Trouver toutes les colonnes de la ligne
      if len(cols) > 10:  # Vérifier si la ligne contient plus de 10 colonnes (pour s'assurer qu'elle contient des données météorologiques)
        day = cols[0].text.strip()  # Extraire le jour de la colonne 0 et supprimer les espaces inutiles
        time = cols[1].text.strip()  # Extraire l'heure de la colonne 1 et supprimer les espaces inutiles
        temp = cols[2].text.strip().split(' ')[0]  # Extraire la température de la colonne 2, supprimer les espaces inutiles et prendre seulement la partie avant l'espace
        wind_direction = cols[4].find('img')['title']  # Trouver l'élément img dans la colonne 4 et extraire le titre (direction du vent)
        wind_speed = cols[5].text.strip()  # Extraire la vitesse du vent de la colonne 5 et supprimer les espaces inutiles
        wind_gust = cols[6].text.strip()  # Extraire les rafales de vent de la colonne 6 et supprimer les espaces inutiles
        rain = cols[7].text.strip()  # Extraire les précipitations de la colonne 7 et supprimer les espaces inutiles
        humidity = cols[8].text.strip()  # Extraire l'humidité de la colonne 8 et supprimer les espaces inutiles
        pressure = cols[9].text.strip()  # Extraire la pression de la colonne 9 et supprimer les espaces inutiles
        weather = cols[10].find('img')['title']  # Trouver l'élément img dans la colonne 10 et extraire le titre (conditions météorologiques)
        
        # Ajouter les données extraites à la liste des données
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
    
    return data

# Lire le fichier JSON existant
with open('locationsWeather.json', 'r', encoding='utf-8') as file:
    locations_data = json.load(file)

# Scraper les données pour chaque localité
for location in locations_data['locationsWeather']:
    print(f"Scraping weather data for {location['name']}...")
    weather_data = scrape_weather_data(location['url'])
    location['weather_data'] = weather_data

# Écrire les données mises à jour dans le fichier JSON
with open('locationsWeather.json', 'w', encoding='utf-8') as file:
    json.dump(locations_data, file, ensure_ascii=False, indent=4)

print("Les données météo ont été mises à jour dans 'locationsWeather.json'")
