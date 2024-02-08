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

pygame.mixer.music.load("chnason_menu.mp3")
pygame.mixer.music.play(-1)

# Chargement du fond
fond = pygame.image.load("pokemon_backgrourn_menu.png")
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Chargement de l'image de titre
titre_image = pygame.image.load("logo.png")
titre_image = pygame.transform.scale(titre_image, (400, 100))


def main():
    menu = MenuPokemon(largeur, hauteur)

    while True:
       

        menu.afficher(fenetre, fond, titre_image)     
        bouton_clic = menu.gerer_evenements(pygame.event.poll())



        for event in pygame.event.get():
    # Si l'utilisateur ferme la fenêtre, quitte le programme
            if event.type == pygame.QUIT:
                pygame.quit()

            # Si la touche ESC est enfoncée, quitte le programme
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris

                    # Si le clic est dans la zone du bouton "Retour au menu"
                    if 200 <= event.pos[0] <= 600 and 250 <= event.pos[1] <= 300:
                        print("Clic sur le bouton 'Retour au menu'")

                    # Si le clic est dans la zone du Pokémon 1
                    if 199 <= event.pos[0] <= 600 and 324<= event.pos[1] <= 374 :
                        print("Clic sur le Pokémon 1")

                    # Si le clic est dans la zone du Pokémon 2
                    if 200 <= event.pos[0] <= 600 and  400<= event.pos[1] <= 450:
                        print("Clic sur le Pokémon 2")

                    # Si le clic est dans la zone du Pokémon 3
                    if 200 <= event.pos[0] <= 600 and 475 <= event.pos[1] <= 525:
                        print("Clic sur le Pokémon 3")

if __name__ == "__main__":
    main()

