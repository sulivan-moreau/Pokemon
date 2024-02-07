import tkinter as tk
from PIL import Image, ImageTk
import json

root = tk.Tk()
root.title("Pokédex")

try:
    with open('/Users/sulivanmoreau/Pokemon/Data/Pokeedex.json', 'r', encoding='utf-8') as file:
        pokemon_data = json.load(file)
except Exception as e:
    print(f"Erreur lors du chargement du fichier JSON : {e}")
    exit(1)

def search_pokemon():
    query = search_entry.get().strip().capitalize()
    data = pokemon_data.get(query)
    if data:
        info = f"Nom: {query}\nNuméro: {', '.join(data['Numéro'])}\nPV: {', '.join(data['PV'])}\n"
        info += f"Attaque: {', '.join(data['Attaque'])}\nDéfense: {', '.join(data['Défense'])}\n"
        info += f"Attaque Spéciale: {', '.join(data['Attaque Spéciale'])}\nDéfense Spéciale: {', '.join(data['Défense Spéciale'])}\n"
        info += f"Vitesse: {', '.join(data['Vitesse'])}\nTypes: {', '.join(data['Types'])}\n"
        if data['Evolution']:
            info += f"Evolution: {', '.join(data['Evolution'])}\n"
        if data['Niveau']:
            info += f"Niveau d'évolution: {', '.join(data['Niveau'])}\n"
        chemin_dossier_images = '/Users/sulivanmoreau/Pokemon/img'
        chemin_image = f"{chemin_dossier_images}/{data['Numéro'][0].zfill(3)}.png"
        image = Image.open(chemin_image)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        result_label.config(text=info)
    else:
        result_label.config(text="Pokémon non trouvé")
        image_label.config(image='')

image_label = tk.Label(root)
image_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Rechercher", command=search_pokemon)
search_button.pack()

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

root.mainloop()