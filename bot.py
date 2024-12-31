import requests
import os

# Configuration
WEBLATE_URL = "https://hosted.weblate.org"  # Remplacez par votre URL Weblate
API_TOKEN = "wlu_z3oz6rC3VfTBgyeVabKvvs5cf1lB0Tt0b59K"  # Remplacez par votre clé API
PROJECT_SLUG = "dqxfr"  # Slug du projet dans Weblate

# Chemins des dossiers
BASE_FOLDER_PATH = "C:/Users/Sato/Desktop/DQX/dqx_dat_dump-main/tools/packing/new_json/"
JA_FOLDER_PATH = os.path.join(BASE_FOLDER_PATH, "ja")  # Dossier contenant les fichiers source

# Fonction pour créer un composant
def create_component(project_slug, source_file):
    component_name = os.path.basename(source_file).replace(".json", "")
    url = f"{WEBLATE_URL}/api/projects/{project_slug}/components/"
    headers = {
        "Authorization": f"Token {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "name": component_name,
        "slug": component_name.lower().replace(" ", "-"),
        "file_format": "json",
        "source_language": "ja",  # Langue source (japonais)
        "filemask": f"*/{os.path.basename(source_file)}",  # Motif de fichier
        "template": f"ja/{os.path.basename(source_file)}",  # Fichier de base mono-langue
        "repo": "file:///C:/Users/Sato/Desktop/DQX/dqx_dat_dump-main/tools/packing/new_json/.git",  # Dépôt Git local
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Composant créé : {component_name}")
    else:
        print(f"Erreur lors de la création du composant {component_name} : {response.status_code} - {response.text}")

# Créer les composants pour tous les fichiers source
for ja_file in os.listdir(JA_FOLDER_PATH):
    if ja_file.endswith(".json"):
        ja_path = os.path.join(JA_FOLDER_PATH, ja_file)
        create_component(PROJECT_SLUG, ja_path)
