import random 
from pokemon_type import types_pokemon
from Stats import Statistiques

class CapaciteStatistique:

    def get_nom(self):
        return self.nom_stat

    def __init__(self, nom_stat, precision, pp, type_capacite, classe_capacite, effet_statistique):
        self.nom_stat= nom_stat
        self.precision = precision
        self.pp = pp
        self.type_capacite = type_capacite
        self.classe_capacite = classe_capacite
        self.effet_statistique = effet_statistique

    def utiliser(self, attaquant, adversaire):
        # Vérifie si adversaire a un attribut statistiques de type Statistiques
        if hasattr(adversaire, 'statistiques') and isinstance(adversaire.statistiques, Statistiques):
            # Altération des statistiques de l'adversaire
            if self.nom_stat == "Rugissement":
                attaquant.statistiques.baisser_statistiques_aleatoires(statistique_a_baisser="attaque", pourcentage_min=10, pourcentage_max=20)
                return f"L'attaque de {attaquant.nom} baisse."
            elif self.nom_stat == "Mimi-Queue":
                attaquant.statistiques.baisser_statistiques_aleatoires(statistique_a_baisser="defense", pourcentage_min=10, pourcentage_max=20)
                return f"La défense de {attaquant.nom} baisse."

        # Vérifie si l'attaquant a un attribut statistiques de type Statistiques
        if hasattr(attaquant, 'statistiques') and isinstance(attaquant.statistiques, Statistiques):
            # Altération des statistiques de l'attaquant
            if self.nom_stat == "Rugissement":
                adversaire.statistiques.baisser_statistiques_aleatoires(statistique_a_baisser="attaque", pourcentage_min=10, pourcentage_max=20)
                return f"L'attaque de {adversaire.nom} baisse."
            elif self.nom_stat == "Mimi-Queue":
                adversaire.statistiques.baisser_statistiques_aleatoires(statistique_a_baisser="defense", pourcentage_min=10, pourcentage_max=20)
                return f"La défense de {adversaire.nom} baisse."

# Exemple d'instanciation d'une capacité statistique
Rugissement = CapaciteStatistique("Rugissement", 100, 40, "Normal", "Statut", {'statistique': 'Attaque'})
Mimi_Queue = CapaciteStatistique("Mimi-Queue", 100, 30, "Normal", "Statut", {'statistique': 'Defense'})

