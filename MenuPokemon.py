import pygame
from Bouton import Bouton

class MenuPokemon:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.boutons = [
         Bouton("Nouvelle Partie", (200, 250), (0, 128, 0)),  # Vert foncé
    Bouton("Continuer", (200, 325), (0, 128, 0)),  # Vert foncé
    Bouton("Pokédex", (200, 400), (0, 128, 0)),  # Vert foncé
    Bouton("Quitter", (200, 475), (0, 128, 0)) 
        ]

    def afficher(self, fenetre, fond, titre_image):
        fenetre.blit(fond, (0, 0))
        fenetre.blit(titre_image, (self.largeur // 2 - 200, self.hauteur // 4 - 50))

        for bouton in self.boutons:
            bouton.afficher(fenetre)

        pygame.display.flip()

    def gerer_evenements(self, evenement):
        if evenement.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            for bouton in self.boutons:
                if bouton.collision(evenement.pos):
                    return bouton
        elif evenement.type == pygame.MOUSEMOTION:
            for bouton in self.boutons:
                if bouton.collision(evenement.pos):
                    bouton.survol()
                else:
                    bouton.non_survol()
        return None

    def afficher(self, fenetre, fond, titre_image):
        fenetre.blit(fond, (0, 0))
        fenetre.blit(titre_image, (self.largeur // 2 - 200, self.hauteur // 4 - 50))

        for bouton in self.boutons:
            bouton.afficher(fenetre)

        pygame.display.flip()

    def gerer_evenements(self, evenement):
        if evenement.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            for bouton in self.boutons:
                if bouton.collision(evenement.pos):
                    return bouton
        elif evenement.type == pygame.MOUSEMOTION:
            for bouton in self.boutons:
                if bouton.collision(evenement.pos):
                    bouton.survol()
                else:
                    bouton.non_survol()
        return None