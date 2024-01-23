import pygame
from MenuPokemon import MenuPokemon

pygame.init()

# Dimensions de la fenêtre
largeur = 800
hauteur = 600

# Couleurs
blanc = (255, 255, 255)

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Menu Pokémon")

# Chargement du fond
fond = pygame.image.load("pokemon_backgrourn_menu.png")
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Chargement de l'image de titre
titre_image = pygame.image.load("logo.png")
titre_image = pygame.transform.scale(titre_image, (400, 100))


def main():
    menu = MenuPokemon(largeur, hauteur)

    while True:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                quit()

        menu.afficher(fenetre, fond, titre_image)
        bouton_clic = menu.gerer_evenements(pygame.event.poll())

        if bouton_clic:
            if bouton_clic.texte_surface.get_text() == "Nouvelle Partie":
                print("Nouvelle partie !")
                # Remettre le Pokédex à zéro ici
            elif bouton_clic.texte_surface.get_text() == "Continuer":
                print("Continuer la partie")
                # Ajoutez le code pour charger la sauvegarde existante
            elif bouton_clic.texte_surface.get_text() == "Pokédex":
                print("Pokédex !")
                # Ajoutez le code pour ouvrir le Pokédex
            elif bouton_clic.texte_surface.get_text() == "Quitter":
                pygame.quit()
                quit()

if __name__ == "__main__":
    main()

