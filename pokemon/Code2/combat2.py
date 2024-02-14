import json
import sys
import random
import pygame
from Starter import *

pygame.init()

class Pokemon:
    def __init__(self, nom, data):
        self.nom = nom
        self.data = data

    def afficher_image(self, x, y):
        # Charger l'image du Pokémon
        image_path = self.data["Img"][0]
        image = pygame.image.load(image_path)
        # Afficher l'image à la position (x, y)
        fenetre.blit(image, (x, y))

    def afficher_statistiques(self, x, y):
        # Afficher les statistiques du Pokémon à la position (x, y)
        font = pygame.font.Font(None, 36)
        pv_text = font.render(f"PV: {self.data['PV'][0]}", True, (255, 255, 255))
        attaque_text = font.render(f"Attaque: {self.data['Attaque'][0]}", True, (255, 255, 255))
        defense_text = font.render(f"Défense: {self.data['Défense'][0]}", True, (255, 255, 255))
        # Afficher les textes à la position (x, y)
        fenetre.blit(pv_text, (x, y))
        fenetre.blit(attaque_text, (x, y + 40))
        fenetre.blit(defense_text, (x, y + 80))

    def afficher_details(self, x, y):
        # Afficher les détails du Pokémon à la position (x, y)
        font = pygame.font.Font(None, 36)
        nom_text = font.render(f"Nom: {self.nom}", True, (255, 255, 255))
        numero_text = font.render(f"Numéro: {self.data['Numéro'][0]}", True, (255, 255, 255))
        types_text = font.render(f"Types: {', '.join(self.data['Types'])}", True, (255, 255, 255))
        # Afficher les textes à la position (x, y)
        fenetre.blit(nom_text, (x, y))
        fenetre.blit(numero_text, (x, y + 40))
        fenetre.blit(types_text, (x, y + 80))


with open('pokedex.json', 'r') as file:
    pokedex_data = json.load(file)

# Récupérer la liste des noms de Pokémon
pokemon_names = list(pokedex_data.keys())

def choisir_pokemon():
    # Récupérer trois Pokémon aléatoires
    pokemons_aleatoires = random.sample(pokemon_names, 3)

    # Créer des objets Pokémon à partir des données JSON
    pokemons = [Pokemon(pokemon_name, pokedex_data[pokemon_name]) for pokemon_name in pokemons_aleatoires]
    choix = 0  # Indice du Pokémon sélectionné
    x_position = 50  # Position x de l'affichage des Pokémon
    selection_effectuee = False

    while not selection_effectuee:
        fenetre.fill(NOIR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    x, y = event.pos
                    # Vérifier si le clic est sur l'image d'un Pokémon
                    for i, pokemon in enumerate(pokemons):
                        pokemon_x = 50 + i * (200 + 50)
                        pokemon_rect = pygame.Rect(pokemon_x, 200, 200, 200)
                        if pokemon_rect.collidepoint(x, y):
                            choix = i
                            selection_effectuee = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    choix = (choix + 1) % len(pokemons)
                elif event.key == pygame.K_LEFT:
                    choix = (choix - 1) % len(pokemons)
                elif event.key == pygame.K_SPACE:
                    selection_effectuee = True  # Appuyer sur la barre d'espace pour confirmer le choix

            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                # Vérifier si la souris survole l'image d'un Pokémon
                for i, pokemon in enumerate(pokemons):
                    pokemon_x = 50 + i * (200 + 50)
                    pokemon_rect = pygame.Rect(pokemon_x, 200, 200, 200)
                    if pokemon_rect.collidepoint(x, y):
                        choix = i

        # Afficher les choix même pendant la sélection
        for i, pokemon in enumerate(pokemons):
            pokemon_x = 50 + i * (200 + 50)
            pokemon.afficher_image(pokemon_x, 200)
            pokemon.afficher_statistiques(pokemon_x, 170)

        pokemons[choix].afficher_details(0, 0)
        
        pygame.draw.rect(fenetre, ROUGE, (50 + choix * (200 + 50), 200, 200, 200), 2)

        pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()