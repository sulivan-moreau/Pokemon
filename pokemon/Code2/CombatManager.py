

import pygame
import sys
import random
import time
from GameManager import GameManager
from fenetre import *
from Capacité import *
from Capacite_stats import *
pygame.mixer.init

class CombatManager:

    
    def __init__(self, pokemon_joueur, pokemon_adversaire):
        self.pokemon_joueur = pokemon_joueur
        self.pokemon_adversaire = pokemon_adversaire
        self.attaque_selectionnee = None
        self.font = pygame.font.Font(None, 36)
        self.etat_combat = "ChoixAttaque"
        self.image_terrain_combat = pygame.image.load("Code2/d6ihzl8-b9dca60e-2a9e-4b18-beed-44725b4d1d37.png")
        self.image_terrain_combat = pygame.transform.scale(self.image_terrain_combat, (largeur, hauteur))
        self.position_pokemon_joueur = (200, 200)
        self.position_pokemon_adversaire = (largeur - 250, 400)

    def jouer_musique_combat(self):
        pygame.mixer.music.load("Code2/onlymp3.to - Pokémon HeartGold SoulSilver Suicune Battle Music HQ -ok3_XzQWr-s-192k-1706198681.mp3")
        pygame.mixer.music.play(-1)

    def arreter_musique_combat(self):
        pygame.mixer.music.stop()

    def initialiser(self):
        self.fenetre.main_loop(self.boucle_principale)

    def afficher_message_progressif(self, message):
        pygame.draw.rect(fenetre, BLANC, (50, 20, largeur - 100, 50))  # Boîte blanche
        font = pygame.font.Font(None, 36)
        
        message_affichage = ""
        for char in message:
            message_affichage += char
            texte_message = font.render(message_affichage, True, NOIR)
            fenetre.blit(texte_message, (60, 30))  # Ajustez la position Y selon vos préférences
            pygame.display.flip()
            pygame.time.delay(100)

    def dessiner_arriere_plan(self):
        # Charger l'image de fond
        fond = pygame.image.load("Code2/d6ihzl8-b9dca60e-2a9e-4b18-beed-44725b4d1d37.png")  # Remplacez par le chemin de votre image

        # Redimensionner l'image pour qu'elle corresponde à la taille de la fenêtre
        fond = pygame.transform.scale(fond, (largeur, hauteur))

        # Afficher l'image à la position (0, 0)
        fenetre.blit(fond, (0, 0))

        pygame.display.flip()

    def tour_joueur(self):
        attaque_selectionnee = None

        while attaque_selectionnee is None:
            attaque_selectionnee = self.choisir_attaque_clavier()
            if attaque_selectionnee is not None:
                break

        self.attaque_selectionnee = attaque_selectionnee

        if self.attaque_selectionnee is not None:
            capacite_joueur = self.pokemon_joueur.capacites[self.attaque_selectionnee]

            if self.attaque_selectionnee is not None:
                capacite_joueur = self.pokemon_joueur.capacites[self.attaque_selectionnee]

                if isinstance(capacite_joueur, Capacite):
                    degats_joueur = capacite_joueur.utiliser(self.pokemon_joueur, self.pokemon_adversaire)
                    message_joueur = f"{self.pokemon_joueur.nom} utilise {capacite_joueur.get_nom()} et inflige {degats_joueur} dégâts !"
                    message_joueur_2 = f"{self.pokemon_adversaire.nom} perd {degats_joueur} PV !"

                # Dans la méthode tour_joueur
                elif isinstance(capacite_joueur, CapaciteStatistique):
                    capacite_joueur.utiliser(self.pokemon_adversaire, self.pokemon_joueur)
                    message_joueur = f"{self.pokemon_joueur.nom} utilise {capacite_joueur.get_nom()}"

                    effet_statistique = capacite_joueur.effet_statistique

                    if capacite_joueur.get_nom() == "Rugissement":
                        message_joueur_2 = f"L'attaque de {self.pokemon_adversaire.nom} baisse !"
                    elif capacite_joueur.get_nom() == "Mimi-Queue":
                        message_joueur_2 = f"La défense de {self.pokemon_adversaire.nom} baisse !"

                self.position_pokemon_joueur = (200, 200)
                self.position_pokemon_adversaire = (largeur - 250, 400)

                # Affichage des PV et message
                self.afficher_statut_combat()


                self.afficher_message_progressif(message_joueur)
                self.afficher_message_progressif(message_joueur_2)
                time.sleep(2)

                # Messages de débogage
            print(f"Message joueur: {message_joueur}")
            print(f"Message joueur 2: {message_joueur_2}")

    def attaque_adversaire(self):
        capacite_adversaire = random.choice(self.pokemon_adversaire.capacites)

        if isinstance(capacite_adversaire, Capacite):
            degats_adversaire = capacite_adversaire.utiliser(self.pokemon_adversaire, self.pokemon_joueur)
            message = f"{self.pokemon_adversaire.nom} utilise {capacite_adversaire.get_nom()} et inflige {degats_adversaire} dégâts !"
            message2 = f"{self.pokemon_joueur.nom} perd {degats_adversaire} PV !"

        elif isinstance(capacite_adversaire, CapaciteStatistique):
            capacite_adversaire.utiliser(self.pokemon_adversaire, self.pokemon_joueur)
            message = f"{self.pokemon_adversaire.nom} utilise {capacite_adversaire.get_nom()}"

            if capacite_adversaire.get_nom() == "Rugissement":
                message2 = f"L'attaque de {self.pokemon_joueur.nom} baisse !"
            elif capacite_adversaire.get_nom() == "Mimi-Queue":
                message2 = f"La défense de {self.pokemon_joueur.nom} baisse !"

        self.position_pokemon_joueur = (200, 200)
        self.position_pokemon_adversaire = (largeur - 250, 400)

            # Affichage des PV et message
        self.afficher_statut_combat()


        self.afficher_message_progressif(message)
        self.afficher_message_progressif(message2)
        time.sleep(2)

        self.afficher_statut_combat()

    def tour_adversaire(self):
        self.attaque_adversaire()
        self.afficher_menu_attaques()

    def combat(self):
        self.jouer_musique_combat()

        while self.pokemon_joueur.statistiques.points_de_vie > 0 and self.pokemon_adversaire.statistiques.points_de_vie > 0:
            attaquant, defenseur = self.determiner_ordre_attaque()

            if self.etat_combat == "ChoixAttaque":
                self.afficher_message_progressif("Choisissez une attaque")
                self.attaque_selectionnee = self.choisir_attaque()

            # Attaque de l'adversaire
            self.attaque_adversaire()

            # Affichage des PV et message
            self.afficher_statut_combat()

            if self.pokemon_joueur.statistiques.points_de_vie <= 0:
                self.etat_combat = "FinCombat"
                self.afficher_message_progressif(f"{self.pokemon_adversaire.nom} a gagné !")
                break

            if self.pokemon_adversaire.statistiques.points_de_vie <= 0:
                self.etat_combat = "FinCombat"
                self.afficher_message_progressif(f"{self.pokemon_joueur.nom} a gagné !")
                break

        self.arreter_musique_combat()

        # Afficher le message du vainqueur après la boucle de combat
        pygame.display.flip()
        pygame.time.Clock().tick(5)  # Ajout d'une attente pour limiter la fréquence d'actualisation
        self.afficher_message_progressif(f"{self.pokemon_joueur.nom} a gagné !")


    def afficher_statut_combat(self):
        fenetre.fill(NOIR)
        self.dessiner_arriere_plan()
        fond = pygame.image.load("Code2/d6ihzl8-b9dca60e-2a9e-4b18-beed-44725b4d1d37.png")  # Remplacez par le chemin de votre image

        # Redimensionner l'image pour qu'elle corresponde à la taille de la fenêtre
        fond = pygame.transform.scale(fond, (largeur, hauteur))

        # Afficher l'image à la position (0, 0)
        fenetre.blit(fond, (0, 0))

        pygame.display.flip()

        self.pokemon_joueur.afficher_image(250, 400)
        self.pokemon_joueur.afficher_statistiques(170, 350)
        self.pokemon_adversaire.afficher_image(largeur - 300, 170)
        self.pokemon_adversaire.afficher_statistiques(largeur - 300, 140)
        for i, attaque in enumerate(self.pokemon_joueur.capacites):
            rect = pygame.Rect(50, 400 + i * 30, 200, 30)
            pygame.draw.rect(fenetre, ROUGE if i == self.attaque_selectionnee else BLANC, rect, 2)
            texte_attaque = self.font.render(attaque.get_nom(), True, BLANC)
            fenetre.blit(texte_attaque, (rect.x + 5, rect.y + 5))

        if self.etat_combat == "ChoixAttaque":
            self.afficher_box("Choisissez une attaque")
        elif self.etat_combat == "FinCombat":
            self.afficher_box(f"{self.pokemon_joueur.nom} a gagné !")

        # Affichage des PV et message
        self.afficher_pv()

        pygame.display.flip()
        pygame.time.Clock().tick(5)

        if self.pokemon_joueur.statistiques.points_de_vie <= 0:
            self.etat_combat = "FinCombat"
            self.afficher_box(f"{self.pokemon_adversaire.nom} a gagné !")

    def afficher_pv(self):
        # Définir la largeur et la hauteur de la boîte des PV
        largeur_boite_pv = 100
        hauteur_boite_pv = 50

        # Boîte complètement transparente avec coins arrondis
        surface_pv_joueur = pygame.Surface((largeur_boite_pv, hauteur_boite_pv), pygame.SRCALPHA)
        surface_pv_adversaire = pygame.Surface((largeur_boite_pv, hauteur_boite_pv), pygame.SRCALPHA)

        # Dessiner les coins arrondis sur la boîte du joueur
        pygame.draw.rect(surface_pv_joueur, (255, 255, 255, 0), (0, 0, largeur_boite_pv, hauteur_boite_pv), border_radius=10)
        # Dessiner les coins arrondis sur la boîte de l'adversaire
        pygame.draw.rect(surface_pv_adversaire, (255, 255, 255, 0), (0, 0, largeur_boite_pv, hauteur_boite_pv), border_radius=10)

        # Positionner la boîte des PV du joueur
        position_boite_pv_joueur = (largeur - largeur_boite_pv - 630, hauteur - hauteur_boite_pv - 186)
        fenetre.blit(surface_pv_joueur, position_boite_pv_joueur)

        # Positionner la boîte des PV de l'adversaire (ajustée vers le haut et un peu à gauche)
        position_boite_pv_adversaire = (largeur - largeur_boite_pv - 300, hauteur - hauteur_boite_pv - 400)
        fenetre.blit(surface_pv_adversaire, position_boite_pv_adversaire)

        font = pygame.font.Font(None, 36)
        texte_pv_joueur = font.render(f"PV: {self.pokemon_joueur.statistiques.points_de_vie}", True, NOIR)
        texte_pv_adversaire = font.render(f"PV: {self.pokemon_adversaire.statistiques.points_de_vie}", True, NOIR)

        # Positionner le texte à droite de la boîte des PV du joueur
        position_texte_pv_joueur = (position_boite_pv_joueur[0] + 10, position_boite_pv_joueur[1] - 10)
        fenetre.blit(texte_pv_joueur, position_texte_pv_joueur)

        # Positionner le texte à gauche et un peu plus haut de la boîte des PV de l'adversaire
        position_texte_pv_adversaire = (position_boite_pv_adversaire[0] + 10, position_boite_pv_adversaire[1] - 10)
        fenetre.blit(texte_pv_adversaire, position_texte_pv_adversaire)


    def main(self):
        pygame.display.flip()
        self.pokemon_joueur = GameManager().choisir_pokemon()
        self.pokemon_adversaire = GameManager().choisir_pokemon()
        self.jouer_musique_combat()
        self.animation_flash_combat()

        font = pygame.font.Font(None, 36)  # Ajout de cette ligne pour définir la police

        # Boucle principale
        while self.pokemon_joueur.statistiques.points_de_vie > 0 and self.pokemon_adversaire.statistiques.points_de_vie > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.attaque_selectionnee is not None:
                            self.combat()
                            self.attaque_selectionnee = None

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Bouton gauche de la souris
                        x, y = event.pos
                        # Vérifier si le clic est sur une attaque
                        for i, attaque in enumerate(self.pokemon_joueur.capacites):
                            attaque_rect = pygame.Rect(50, 400 + i * 30, 200, 30)
                            if attaque_rect.collidepoint(x, y):
                                self.attaque_selectionnee = i

            self.afficher_combat_face_a_face()

            fond = pygame.image.load("Code2/d6ihzl8-b9dca60e-2a9e-4b18-beed-44725b4d1d37.png")
            fond = pygame.transform.scale(fond, (largeur, hauteur))
            fenetre.blit(fond, (0, 0))

            self.pokemon_joueur.afficher_image(250, 400)
            self.pokemon_joueur.afficher_statistiques(170, 350)
            self.pokemon_adversaire.afficher_image(largeur - 300, 170)
            self.pokemon_adversaire.afficher_statistiques(largeur - 300, 140)

            for i, attaque in enumerate(self.pokemon_joueur.capacites):
                rect = pygame.Rect(50, 400 + i * 30, 200, 30)
                pygame.draw.rect(fenetre, ROUGE if i == self.attaque_selectionnee else BLANC, rect, 2)
                texte_attaque = font.render(attaque.get_nom(), True, BLANC)
                fenetre.blit(texte_attaque, (rect.x + 5, rect.y + 5))

            self.afficher_message_progressif("Choisir une attaque !")

            # Affichage des boîtes des PV
            self.afficher_pv()

            pygame.display.flip()
            pygame.time.Clock().tick(5)

            if self.pokemon_joueur.statistiques.points_de_vie <= 0:
                self.afficher_message_progressif(f"{self.pokemon_adversaire.nom} a gagné !")
                break

            # Tour du joueur
            self.tour_joueur()

            # Tour de l'adversaire
            self.tour_adversaire()


        self.afficher_message_progressif(f"{self.pokemon_joueur.nom} a gagné !")
        pygame.display.flip()
        pygame.time.Clock().tick(5)

    def afficher_menu_attaques(self):
        font = pygame.font.Font(None, 36)
        attaques = self.pokemon_joueur.capacites

        # Définir les nouvelles dimensions du tableau
        largeur_tableau = 250
        hauteur_tableau = 50
        espace_entre_attaques = 10

        # Définir la position et les dimensions du tableau
        x_tableau = (largeur - largeur_tableau - 50)  # Ajustez la valeur pour déplacer vers la droite
        y_tableau = hauteur - hauteur_tableau - 20

        # Calculer les coordonnées de chaque case d'attaque dans le tableau
        for i, attaque in enumerate(attaques):
            x_case = x_tableau
            y_case = y_tableau + i * (hauteur_tableau + espace_entre_attaques)

            # Choisir une couleur d'arrière-plan différente pour chaque capacité
            couleur_arriere_plan = (150, 150, 150)  # Vous pouvez ajuster les valeurs RVB selon votre choix

            # Dessiner la case d'attaque avec la couleur d'arrière-plan
            pygame.draw.rect(fenetre, couleur_arriere_plan, (x_case, y_case, largeur_tableau, hauteur_tableau))

            # Rendre le texte de l'attaque avec la couleur du texte blanche
            texte_attaque = font.render(f"{i + 1}. {attaque.get_nom()}", True, BLANC)

            # Afficher le texte sur la fenêtre de jeu
            fenetre.blit(texte_attaque, (x_case + 10, y_case + 10))



    def choisir_attaque(self):
        attaque_selectionnee = None

        while not attaque_selectionnee:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Bouton gauche de la souris
                        x, y = event.pos
                        attaque_selectionnee = self.verifier_clic_attaque(x, y)

            # Affichage en cours de choix d'attaque
            self.afficher_statut_combat()

        return attaque_selectionnee

    def verifier_clic_attaque(self, x, y):
        attaques = self.pokemon_joueur.capacites

        for i, attaque in enumerate(attaques):
            attaque_rect = pygame.Rect(50, 400 + i * 30, 200, 30)
            if attaque_rect.collidepoint(x, y):
                return i

        return None

    def choisir_attaque_clavier(self):
        attaques = self.pokemon_joueur.capacites

        selection_effectuee = False
        attaque_selectionnee = None

        while not selection_effectuee:
            #fenetre.fill(NOIR)

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
                                attaque_selectionnee = i
                                selection_effectuee = True

            self.pokemon_joueur.afficher_image(250, 400)
            self.pokemon_joueur.afficher_statistiques(170, 350)
            self.pokemon_adversaire.afficher_image(largeur - 300, 170)
            self.pokemon_adversaire.afficher_statistiques(largeur - 300, 140)

            # Afficher les attaques
            for i, attaque in enumerate(attaques):
                pygame.draw.rect(fenetre, ROUGE if i == attaque_selectionnee else BLANC, (50, 400 + i * 30, 200, 30), 2)
                texte_attaque = self.font.render(attaque.get_nom(), True, BLANC)
                fenetre.blit(texte_attaque, (55, 400 + i * 30 + 5))

            pygame.display.flip()
            pygame.time.Clock().tick(30)

        return attaque_selectionnee

    def determiner_ordre_attaque(self):
        if self.pokemon_joueur.statistiques.vitesse > self.pokemon_adversaire.statistiques.vitesse:
            return self.pokemon_joueur, self.pokemon_adversaire
        elif self.pokemon_joueur.statistiques.vitesse < self.pokemon_adversaire.statistiques.vitesse:
            return self.pokemon_adversaire, self.pokemon_joueur
        else:
            # Égalité de vitesse, utilisez la randomisation
            return random.sample([self.pokemon_joueur, self.pokemon_adversaire], 2)

    
    def afficher_box(self, message):
        pygame.draw.rect(fenetre, BLANC, (50, 20, largeur - 100, 50))  # Boîte blanche
        font = pygame.font.Font(None, 36)
        texte_message = font.render(message, True, NOIR)
        fenetre.blit(texte_message, (60, 30))  # Ajustez la position Y selon vos préférences
        pygame.display.flip()  # Ajout de cette ligne pour afficher immédiatement la boîte


    def afficher_combat_face_a_face(self, couleur_arriere_plan=None):
        self.dessiner_arriere_plan()

        self.pokemon_joueur.afficher_image(250, 400)
        self.pokemon_joueur.afficher_statistiques(170, 350)
        self.pokemon_adversaire.afficher_image(largeur - 300, 170)
        self.pokemon_adversaire.afficher_statistiques(largeur - 300, 140)

        pygame.display.flip()

        if couleur_arriere_plan:
            fenetre.fill(couleur_arriere_plan)


    
    def animation_flash_combat(self):
        # Couleurs pour le flash
        couleur_flash1 = (255, 255, 255)  # Blanc
        couleur_flash2 = (0, 255, 0)  # Vert
        couleur_flash3 = (0, 0, 255)

        duree_flash = 300  # Durée en millisecondes de chaque étape du flash
        nombre_flash = 2   # Nombre de flash avant le début du combat

        for _ in range(nombre_flash):
            # Flash vers couleur 1
            self.afficher_combat_face_a_face(couleur_flash1)
            pygame.display.flip()
            pygame.time.delay(duree_flash)

            # Flash vers couleur 2
            self.afficher_combat_face_a_face(couleur_flash2)
            pygame.display.flip()
            pygame.time.delay(duree_flash)

            self.afficher_combat_face_a_face(couleur_flash3)
            pygame.display.flip()
            pygame.time.delay(duree_flash)

        # Réinitialiser à la couleur d'origine
        self.afficher_combat_face_a_face()  # Utilisez la fonction sans argument pour réinitialiser la couleur
        pygame.display.flip()



