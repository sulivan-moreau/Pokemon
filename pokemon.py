import pygame
import sys
import random
from Stats import Statistiques
from fenetre import *
from pokemon_type import types_pokemon


class Pokemon:
    def __init__(self, nom, type_pokemon, image, capacites, capacites_stats):
        self.nom = nom
        self.type = type_pokemon
        self.image = image
        self.capacites = capacites  # Liste de Capacite
        self.capacites.extend(capacites_stats)  # Ajouter les capacités statistiques à la liste
        self.niveau = 5
        self.statistiques = Statistiques()



    def afficher_info(self):
        return f"Nom: {self.nom}, Type: {self.type}"

    def afficher_image(self, x, y):
        fenetre.blit(self.image, (x, y))

    def afficher_statistiques(self, x, y):
        pygame.draw.rect(fenetre, NOIR, (x, y, 200, 30))  # Fond noir
        pygame.draw.rect(fenetre, VERT, (x, y, (self.statistiques.points_de_vie / 20) * 200, 30))  # Jauge verte

    def afficher_details(self, x, y):
        font = pygame.font.Font(None, 36)
        attributs = [
            ("attaque", self.statistiques.attaque),
            ("défense", self.statistiques.defense),
            ("attaque spéciale", self.statistiques.attaque_speciale),
            ("défense spéciale", self.statistiques.defense_speciale),
            ("vitesse", self.statistiques.vitesse),
        ]

        pygame.draw.rect(fenetre, NOIR, (x, y, 200, 150))
        for i, (attribut, valeur) in enumerate(attributs):
            texte_attribut = font.render(f"{attribut}: {valeur}", True, BLANC)  # Utiliser BLANC ici
            fenetre.blit(texte_attribut, (x + 5, y + i * 30 + 5))


    def utiliser(self, adversaire):
        # Sélectionnez une capacité au hasard parmi celles du Pokémon
        capacite_choisie = random.choice(self.capacites)

        # Appel de la méthode utiliser de la capacité sélectionnée
        degats, effet_statistique = capacite_choisie.utiliser(self, adversaire)


        # Appliquer les dégâts
        adversaire.statistiques.points_de_vie -= degats

        # Imprimer les informations sur l'action
        print(f"Type Capacité: {capacite_choisie.type_capacite}")
        print(f"Type Adversaire: {adversaire.type}")

        # Appliquer les effets statistiques si présents
        if effet_statistique:
            adversaire.appliquer_effet_statistique(effet_statistique)

    def appliquer_effet_statistique(self, effet_statistique):
        stat_a_modifier = effet_statistique['statistique']
        pourcentage_modification = effet_statistique['pourcentage']

        if stat_a_modifier == 'attaque':
            self.statistiques.attaque -= int(self.statistiques.attaque * (pourcentage_modification / 100))
        elif stat_a_modifier == 'defense':
            self.statistiques.defense -= int(self.statistiques.defense * (pourcentage_modification / 100))
            
    def infliger_degats(self, degats):
        # Appliquer les dégâts au Pokémon
        self.statistiques.points_de_vie = max(0, self.statistiques.points_de_vie - degats)