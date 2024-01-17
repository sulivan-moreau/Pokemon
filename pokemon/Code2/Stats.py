import random
import pygame


class Statistiques:
    def __init__(self):
        self.points_de_vie = 20
        self.attaque = random.randint(1, 15)
        self.defense = random.randint(1, 15)
        self.attaque_speciale = random.randint(1, 15)
        self.defense_speciale = random.randint(1, 15)
        self.vitesse = random.randint(1, 15)
        self.niveau = 5

    def calculer_degats(self, attaquant, capacite, adversaire):
        # Statistiques d'attaque et de défense de l'attaquant et de l'adversaire
        att_stat = attaquant.statistiques.attaque
        att_speciale_stat = attaquant.statistiques.attaque_speciale
        def_stat = adversaire.statistiques.defense
        def_speciale_stat = adversaire.statistiques.defense_speciale

        # Choix de la statistique d'attaque en fonction de la classe de la capacité
        if capacite.classe_capacite == "Physique":
            attaque_utilisee = att_stat
            defense_utilisee = def_stat
        else:
            attaque_utilisee = att_speciale_stat
            defense_utilisee = def_speciale_stat

        # Formule pour calculer les dégâts (à ajuster selon vos besoins)
        degats = int(
            ((2 * attaquant.statistiques.points_de_vie / 5 + 2) *
             capacite.puissance * (attaque_utilisee / defense_utilisee)) / 50 + 2
        )

        return degats


