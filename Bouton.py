import pygame

class Bouton:
    def __init__(self, texte, position, couleur):
        self.rect = pygame.Rect(position[0], position[1], 400, 50)
        self.texte_surface = pygame.font.Font(None, 36).render(texte, True, (0, 0, 0))
        self.texte_rect = self.texte_surface.get_rect(center=(position[0] + 200, position[1] + 25))
        self.couleur = couleur
        self.alpha = 255  # Opacité du bouton

    def afficher(self, fenetre):
        surface_bouton = pygame.Surface((400, 50))
        surface_bouton.set_alpha(self.alpha)
        surface_bouton.fill(self.couleur)
        fenetre.blit(surface_bouton, self.rect)
        fenetre.blit(self.texte_surface, self.texte_rect)

    def collision(self, position):
        return self.rect.collidepoint(position)

    def survol(self):
        self.alpha = min(self.alpha + 10, 255)

    def non_survol(self):
        self.alpha = max(self.alpha - 10, 0)
