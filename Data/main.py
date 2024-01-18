import tkinter as tk
import json

# Chargement des données Pokémon à partir du fichier JSON
try:
    with open('/Users/sulivanmoreau/Pokemon/Data/Pokedex_max.json', 'r', encoding='utf-8') as file:
        pokemon_data = json.load(file)
except Exception as e:
    print(f"Erreur lors du chargement du fichier JSON : {e}")
    exit(1)

# Fonction de recherche de Pokémon
def search_pokemon():
    query = search_entry.get().strip()
    # Recherche par nom ou numéro
    for name, data in pokemon_data.items():
        if query.lower() == name.lower() or query == str(data.get('Numero', '')):
            # Formatage des données pour l'affichage
            info = f"Nom: {name}\n"
            info += f"Types: {', '.join(data['Types'])}\n"
            info += f"Statut: {', '.join([f'{k}: {v}' for k, v in data['Statut'].items()])}\n"
            info += f"Evolution: {', '.join(data['Evolution']) if data['Evolution'] else 'Aucune'}\n"
            result_label.config(text=info)
            return
    result_label.config(text="Pokémon non trouvé")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Pokédex")

# Champ de saisie pour la recherche
search_entry = tk.Entry(root)
search_entry.pack()

# Bouton de recherche
search_button = tk.Button(root, text="Rechercher", command=search_pokemon)
search_button.pack()

# Étiquette pour afficher le résultat
result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

# Lancement de l'interface graphique
root.mainloop()
