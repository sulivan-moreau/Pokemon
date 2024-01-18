from pokemon import Pokemon
import pygame
from PIL import Image
from Stats import Statistiques
from fenetre import *

class Salamèche(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Feu", pygame.image.load("resized_autocollant-salameche-pokemon-004.png"), capacites)

    def afficher_image(self, x, y):
        # Votre logique pour afficher l'image de Salamèche
        fenetre.blit(self.image, (x, y))


class Carapuce(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Eau", pygame.image.load("resized_250px-Carapuce-RFVF.png"), capacites)

    def afficher_image(self, x, y):
        # Votre logique pour afficher l'image de Salamèche
        fenetre.blit(self.image, (x, y))


class Bulbizarre(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Plante", pygame.image.load("resized_autocollant-bulbizarre-pokemon-001.png"), capacites)

    def afficher_image(self, x, y):
        # Votre logique pour afficher l'image de Salamèche
        fenetre.blit(self.image, (x, y))