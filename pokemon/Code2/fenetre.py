import pygame

NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)

# Définir la fenêtre (variable globale)
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Choisissez votre Pokémon")