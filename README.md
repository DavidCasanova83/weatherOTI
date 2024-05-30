# weatherOTI

### Pré-requis

Python + venv + pip

1. **Vérifier l'installation de Python**

```bash
python3 --version
```

2. **Installer venv**

```bash
sudo apt-get install python3-venv
```

3. **Créer un environnement virtuel**

```bash
cd /chemin/vers/ton/projet
python3 -m venv myenv
```

4. **Créer un environnement virtuel** :

```bash
source myenv/bin/activate
```

Désactiver l'environnement virtuel dans le terminal d'origine !

```bash
deactivate
```

### Démarrer le projet

1. **Installer les bibliothèques nécessaires** :

pip install requests beautifulsoup4

2. **Créer et exécuter ton script Python** :

   python scrape_weather.py

### Ajouter une location pour récolter les données

Ajouter une location avec ce format dans le locationsWeather.json

```json
{
  "name": "Lyon",
  "postal_code": "69000",
  "url": "https://www.meteociel.fr/previsions/6900/lyon.htm"
}
```

### Améliorations potentielles

- **Automatisation** : Utiliser un planificateur de tâches comme `cron` pour exécuter ce script à intervalles réguliers.
- **Validation des données** : Ajouter des vérifications pour s'assurer que les données extraites sont valides.
- **Notifications** : Intégrer des notifications par email ou SMS en cas de conditions météorologiques spécifiques.
