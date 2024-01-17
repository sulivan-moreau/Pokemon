import pygame
import sys
import random
import time
from GameManager import GameManager
from fenetre import *


class CombatManager:
    def __init__(self, pokemon_joueur, pokemon_adversaire):
        self.pokemon_joueur = pokemon_joueur
        self.pokemon_adversaire = pokemon_adversaire
        self.attaque_selectionnee = None

    def afficher_image(self, x, y):
        fenetre.blit(self.pokemon_joueur.image, (x, y))

    def afficher_menu_attaques(self):
        font = pygame.font.Font(None, 36)
        attaques = self.pokemon_joueur.capacites

        for i, attaque in enumerate(attaques):
            texte_attaque = font.render(f"{i + 1}. {attaque.nom}", True, BLANC)
            capacite_attaque = self.pokemon_joueur.capacites[i]

            fenetre.blit(texte_attaque, (50, 400 + i * 30))

    def afficher_statistiques(self, x, y):
        pygame.draw.rect(fenetre, NOIR, (x, y, 200, 30))  # Fond noir
        pygame.draw.rect(fenetre, VERT, (x, y, (self.statistiques.points_de_vie / 20) * 200, 30))  # Jauge verte

        font = pygame.font.Font(None, 36)
        attributs = [
            ("Attaque", self.statistiques.attaque),
            ("Défense", self.statistiques.defense),
            ("Attaque Spéciale", self.statistiques.attaque_speciale),
            ("Défense Spéciale", self.statistiques.defense_speciale),
            ("Vitesse", self.statistiques.vitesse),
        ]

        pygame.draw.rect(fenetre, NOIR, (x, y + 30, 200, 150))
        for i, (attribut, valeur) in enumerate(attributs):
            texte_attribut = font.render(f"{attribut}: {valeur}", True, BLANC)  # Utiliser BLANC ici
            fenetre.blit(texte_attribut, (x + 5, y + 30 + i * 30 + 5))

    def choisir_attaque_souris(self):
            font = pygame.font.Font(None, 36)
            attaques = self.pokemon_joueur.capacites

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
                            # Vérifier si le clic est sur une attaque
                            for i, attaque in enumerate(attaques):
                                attaque_rect = pygame.Rect(50, 400 + i * 30, 200, 30)
                                if attaque_rect.collidepoint(x, y):
                                    self.attaque_selectionnee = i
                                    selection_effectuee = True

                self.pokemon_joueur.afficher_image(50, 200)
                self.pokemon_joueur.afficher_statistiques(50, 170)
                self.pokemon_adversaire.afficher_image(largeur - 250, 200)
                self.pokemon_adversaire.afficher_statistiques(largeur - 250, 170)

                if self.attaque_selectionnee is not None:
                    pygame.draw.rect(fenetre, ROUGE, (50, 400 + self.attaque_selectionnee * 30, 200, 30), 2)

                self.afficher_menu_attaques()

                pygame.display.flip()
                pygame.time.Clock().tick(30)  # Ajout d'une attente pour limiter la fréquence d'actualisation

    def main(self):
            pygame.display.flip()
            self.pokemon_joueur = GameManager().choisir_pokemon()
            self.pokemon_adversaire = GameManager().choisir_pokemon()

            en_cours = True

            while en_cours:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if self.attaque_selectionnee is not None:
                                self.attaque_selectionnee = None
                                self.combat()
                                en_cours = False
                        elif event.key in [pygame.K_1, pygame.K_2]:
                            self.attaque_selectionnee = int(event.unicode) - 1
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.choisir_attaque_souris()

                fenetre.fill(NOIR)  # Fond noir

                self.pokemon_joueur.afficher_image(50, 200)
                self.pokemon_joueur.afficher_statistiques(50, 170)
                self.pokemon_adversaire.afficher_image(largeur - 250, 200)
                self.pokemon_adversaire.afficher_statistiques(largeur - 250, 170)

                if self.attaque_selectionnee is not None:
                    pygame.draw.rect(fenetre, ROUGE, (50, 400 + self.attaque_selectionnee * 30, 200, 30), 2)

                self.afficher_menu_attaques()

                pygame.display.flip()

    def choisir_attaque(self, indice):
            if 0 <= indice < len(self.pokemon_joueur.capacites):
                self.attaque_selectionnee = indice

    def combat(self):
        while self.pokemon_joueur.statistiques.points_de_vie > 0 and self.pokemon_adversaire.statistiques.points_de_vie > 0:
            # Afficher les informations sur le combat
            print(f"{self.pokemon_joueur.nom} - PV: {self.pokemon_joueur.statistiques.points_de_vie}")
            print(f"{self.pokemon_adversaire.nom} - PV: {self.pokemon_adversaire.statistiques.points_de_vie}")

            # Attaque du joueur
            if self.attaque_selectionnee is not None:
                capacite_joueur = self.pokemon_joueur.choisir_capacite()
                capacite_adversaire = self.pokemon_adversaire.choisir_capacite()
                degats_joueur, effet_statistique_joueur = capacite_joueur.utiliser(self.pokemon_joueur, self.pokemon_adversaire)
                degats_adversaire, effet_statistique_adversaire = capacite_adversaire.utiliser(self.pokemon_adversaire, self.pokemon_joueur)
                print(f"{self.pokemon_joueur.nom} utilise {capacite_joueur.nom} et inflige {degats_joueur} dégâts.")
                time.sleep(1)

            if self.pokemon_adversaire.statistiques.points_de_vie <= 0:
                print(f"{self.pokemon_joueur.nom} a gagné !")
                break

            # Attaque de l'adversaire
            capacite_adversaire = random.choice(self.pokemon_adversaire.capacites)
            if capacite_adversaire:
                degats_adversaire = capacite_adversaire.utiliser(self.pokemon_adversaire, self.pokemon_joueur)
            print(f"{self.pokemon_adversaire.nom} utilise {capacite_adversaire.nom} et inflige {degats_adversaire} dégâts.")
            time.sleep(1)  # Ajouter un délai d'une seconde

            if self.pokemon_joueur.statistiques.points_de_vie <= 0:
                print(f"{self.pokemon_adversaire.nom} a gagné !")
                break

            self.afficher_menu_attaques()

            pygame.display.flip()
