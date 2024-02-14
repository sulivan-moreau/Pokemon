import pygame
import sys
from PIL import Image
from pokemon import Pokemon
from Starter import *
from Capacité import *
from Capacite_stats import CapaciteStatistique
pygame.mixer.init()


def redimensionner_image(image_path, nouvelle_taille):
    img = Image.open(image_path)
    img_resized = img.resize(nouvelle_taille)
    nouveau_chemin = f"resized_{image_path}"
    img_resized.save(nouveau_chemin)
    return pygame.image.load(nouveau_chemin)

image_feu = redimensionner_image("autocollant-salameche-pokemon-004.png", (200, 200))
image_eau = redimensionner_image("250px-Carapuce-RFVF.png", (200, 200))
image_plante = redimensionner_image("autocollant-bulbizarre-pokemon-001.png", (200, 200))


class GameManager:
    def __init__(self):
        self.pokemon_choisi = None
        self.adversaire = None
        self.pokemon_selectionne = 0

    def jouer_musique_choix(self):
        pygame.mixer.music.load("Code2/onlymp3.to - Pokémon Donjon Mystère Soundtrack Grotte Littorale-vD0DsgkOTNg-192k-1706198380.mp3")
        pygame.mixer.music.play(-1)

    def arreter_musique_choix(self):
        pygame.mixer.music.stop()

    def choisir_pokemon(self):
        pokemons = [
            Salamèche("Salamèche", image_feu, [
                Capacite("Charge", 40, 100, 35, "Normal", "Physique"),
                Capacite("Flammèche", 40, 100, 25, "Feu", "Spéciale"),
            ], [
                CapaciteStatistique("Rugissement", 0, 100, 40, "Normal", "Statut"),
            ]),
            Carapuce("Carapuce", image_eau, [
                Capacite("Charge", 40, 100, 35, "Normal", "Physique"),
                Capacite("Pistolet à O", 40, 100, 25, "Eau", "Spéciale"),
            ], [
                CapaciteStatistique("Rugissement", 0, 100, 40, "Normal", "Statut"),
            ]),
            Bulbizarre("Bulbizarre", image_plante, [
                Capacite("Charge", 40, 100, 35, "Normal", "Physique"),
                Capacite("Fouet Lianes", 40, 100, 25, "Plante", "Spéciale"),
            ], [
                CapaciteStatistique("Mimi-Queue", 0, 100, 40, "Normal", "Statut"),
            ]),
        ]

        choix = 0  # Indice du Pokémon sélectionné
        x_position = 50  # Position x de l'affichage des Pokémon
        selection_effectuee = False
        self.jouer_musique_choix()

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
                                self.pokemon_selectionne = i
                                selection_effectuee = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.pokemon_selectionne = (self.pokemon_selectionne + 1) % len(pokemons)
                    elif event.key == pygame.K_LEFT:
                        self.pokemon_selectionne = (self.pokemon_selectionne - 1) % len(pokemons)
                    elif event.key == pygame.K_SPACE:
                        selection_effectuee = True  # Appuyer sur la barre d'espace pour confirmer le choix

                elif event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    # Vérifier si la souris survole l'image d'un Pokémon
                    for i, pokemon in enumerate(pokemons):
                        pokemon_x = 50 + i * (200 + 50)
                        pokemon_rect = pygame.Rect(pokemon_x, 200, 200, 200)
                        if pokemon_rect.collidepoint(x, y):
                            self.pokemon_selectionne = i

            # Afficher les choix même pendant la sélection
            for i, pokemon in enumerate(pokemons):
                pokemon_x = 50 + i * (200 + 50)
                pokemon.afficher_image(pokemon_x, 200)
                pokemon.afficher_statistiques(pokemon_x, 170)

            pokemons[self.pokemon_selectionne].afficher_details(0, 0)
            pygame.draw.rect(fenetre, ROUGE, (50 + self.pokemon_selectionne * (200 + 50), 200, 200, 200), 2)

            pygame.display.flip()

        self.arreter_musique_choix()

        return pokemons[self.pokemon_selectionne]
    