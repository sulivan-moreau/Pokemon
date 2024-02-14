import random

class Statistiques:
    def __init__(self):
        self.points_de_vie = 20
        self.attaque = random.randint(10, 30)
        self.defense = random.randint(10, 30)
        self.attaque_speciale = random.randint(10, 30)
        self.defense_speciale = random.randint(10, 30)
        self.vitesse = random.randint(10, 30)
        self.niveau = 5
        self.statut = 0

    def calculer_degats(self, attaquant, adversaire, capacite):
        att_stat = attaquant.statistiques.attaque
        att_speciale_stat = attaquant.statistiques.attaque_speciale
        def_stat = adversaire.statistiques.defense
        def_speciale_stat = adversaire.statistiques.defense_speciale

        if capacite.classe_capacite == "Physique":
            attaque_utilisee = att_stat
            defense_utilisee = def_stat
        else:
            attaque_utilisee = att_speciale_stat
            defense_utilisee = def_speciale_stat

        # Calcul des dégâts selon la formule avec prise en compte des types
        degats = int(
            (
                (
                    (
                        (
                            (
                                (
                                    (attaquant.niveau * 2 / 5) + 2
                                ) * capacite.puissance * attaque_utilisee / 50
                            ) / defense_utilisee
                        ) * capacite.coup_critique * capacite.r / 100
                    ) + 2
                ) * capacite.stab * capacite.type1_multiplier * capacite.type2_multiplier
            )
        )

        # Dégâts minimum de 1 si le défenseur n'est pas immunisé
        return max(degats, 1)


    # Dans la classe Statistiques
    def baisser_statistiques_aleatoires(self, pourcentage_min, pourcentage_max, statistique_a_baisser):
        valeur_actuelle = getattr(self, statistique_a_baisser.lower())  # Convertir en minuscules
        reduction_min = int(valeur_actuelle * (pourcentage_min / 100))
        reduction_max = int(valeur_actuelle * (pourcentage_max / 100))
        reduction_aleatoire = random.randint(reduction_min, reduction_max)
        nouvelle_valeur = max(0, valeur_actuelle - reduction_aleatoire)
        setattr(self, statistique_a_baisser, nouvelle_valeur)


        print(f"{statistique_a_baisser}: {valeur_actuelle} -> {nouvelle_valeur}")

