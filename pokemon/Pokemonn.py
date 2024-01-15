import pygame
import random
import sys
from PIL import Image
from Type_Pokemon import types_pokemon

pygame.init()

NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)

class Statistiques:
    def __init__(self):
        self.attaque = random.randint(1, 15)
        self.defense = random.randint(1, 15)
        self.attaque_speciale = random.randint(1, 15)
        self.defense_speciale = random.randint(1, 15)
        self.vitesse = random.randint(1, 15)
        self.points_de_vie = 20

class Pokemon:
    def __init__(self, nom, type_pokemon, image):
        self.nom = nom
        self.type_pokemon = type_pokemon
        self.image = image
        self.statistiques = Statistiques()
        self.stats_affichees = True

    def afficher_info(self):
        return f"Nom: {self.nom}, Type: {self.type_pokemon}"

    def afficher_image(self, x, y):
        fenetre.blit(self.image, (x, y))

    def afficher_statistiques(self, x, y):
        pygame.draw.rect(fenetre, NOIR, (x, y, 200, 30))  
        pygame.draw.rect(fenetre, VERT, (x, y, (self.statistiques.points_de_vie / 20) * 200, 30))

    def afficher_details(self, x, y):
        font = pygame.font.Font(None, 36)
        attributs = [
            ("Attaque", self.statistiques.attaque),
            ("Défense", self.statistiques.defense),
            ("Attaque Spéciale", self.statistiques.attaque_speciale),
            ("Défense Spéciale", self.statistiques.defense_speciale),
            ("Vitesse", self.statistiques.vitesse),
        ]

        pygame.draw.rect(fenetre, NOIR, (x, y, 200, 150))
        for i, (attribut, valeur) in enumerate(attributs):
            texte_attribut = font.render(f"{attribut}: {valeur}", True, BLANC)  
            fenetre.blit(texte_attribut, (x + 5, y + i * 30 + 5))

class PokemonFeu(Pokemon):
    def __init__(self, nom, image):
        super().__init__(nom, "Feu", image)

class PokemonEau(Pokemon):
    def __init__(self, nom, image):
        super().__init__(nom, "Eau", image)

class PokemonPlante(Pokemon):
    def __init__(self, nom, image):
        super().__init__(nom, "Plante", image)
