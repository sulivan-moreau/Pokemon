import csv
import json

# Chemin d'accès au fichier CSV
chemin_csv = '/Users/sulivanmoreau/Pokemon/Ressource/BDD.csv'
# Chemin d'accès au nouveau fichier JSON
chemin_json = 'pokeedex.json'

# Lire le fichier CSV et convertir en dictionnaire JSON
pokedex = {}
with open(chemin_csv, mode='r', encoding='utf-8-sig') as fichier_csv:
    lecteur_csv = csv.DictReader(fichier_csv, delimiter=';')  # Notez l'utilisation de delimiter=';'
    for ligne in lecteur_csv:
        nom_pokemon = ligne['Nom']
        pokedex[nom_pokemon] = {
            "Numéro": [ligne['Numéro']],
            "PV": [ligne['Pv']],
            "Attaque": [ligne['Attaque']],
            "Défense": [ligne['Defense']],
            "Attaque Spéciale": [ligne['Sp. Atk']],
            "Défense Spéciale": [ligne['Sp. Def']],
            "Vitesse": [ligne['Speed']],
            "Types": [ligne['Types1']] + [ligne['Types2'].strip()] if ligne.get('Types2', '').strip() else [ligne['Types1']],
            "Evolution": [ligne['Evolution']] if ligne['Evolution'] else [],
            "Niveau": [ligne['Niveau']] if ligne['Niveau'] else [],
            "Img": [f"img/{ligne['Numéro'].zfill(3)}.png"],
            "Theme": ["#FFF140"]
        }

# Écrire le dictionnaire dans un fichier JSON
with open(chemin_json, 'w', encoding='utf-8') as fichier_json:
    json.dump(pokedex, fichier_json, ensure_ascii=False, indent=4)


