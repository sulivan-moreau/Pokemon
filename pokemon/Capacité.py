import random
from Type_Pokemon import types_pokemon

class Capacite:
    def __init__(self, nom, puissance, precision, pp, type_capacite, classe_capacite, effet_statistique=None, niveau_attaquant=5):
        self.nom = nom
        self.puissance = puissance
        self.precision = precision
        self.pp = pp
        self.type_capacite = type_capacite.lower()
        self.classe_capacite = classe_capacite
        self.effet_statistique = effet_statistique

        # Générer un pourcentage aléatoire s'il n'est pas fourni
        if effet_statistique and 'pourcentage' not in effet_statistique:
            self.effet_statistique['pourcentage'] = random.randint(5, 15)

        # Niveau du Pokémon attaquant
        self.niveau_attaquant = niveau_attaquant

    def utiliser(self, attaquant, adversaire):
        # Détermination si l'attaque est physique ou spéciale
        if self.classe_capacite == "Physique":
            att_attaquant = attaquant.statistiques.attaque
            def_adversaire = adversaire.statistiques.defense
        else:
            att_attaquant = attaquant.statistiques.attaque_speciale
            def_adversaire = adversaire.statistiques.defense_speciale

        # Coup critique
        coup_critique = 1
        if random.randint(1, 100) <= 6:  # Remplacez par le calcul réel de la probabilité de coup critique
            coup_critique = 2  # Modifiez selon les règles des jeux Pokémon

        # Calcul du modificateur aléatoire R
        r = random.randint(217, 255) / 255.0  # La formule utilise un nombre aléatoire entre 217 et 255 inclus

        # STAB
        stab = 2 if self.type_capacite in attaquant.type else 1

        # Type de l'attaque par rapport aux types du défenseur
        type1_multiplier = types_pokemon[self.type_capacite].relations[adversaire.type[0].lower()]
        type2_multiplier = 1.0
        if len(adversaire.type) == 2:
            type2_multiplier = types_pokemon[self.type_capacite].relations[adversaire.type[1].lower()]

        # Modificateur MOD1
        mod1 = 1.0  # Remplacez par le calcul réel de MOD1

        # Modificateur MOD2
        mod2 = 1.0  # Remplacez par le calcul réel de MOD2

        # Modificateur MOD3
        mod3 = 1.0  # Remplacez par le calcul réel de MOD3

        # Modificateur global
        modificateur = stab * type1_multiplier * type2_multiplier * coup_critique * r * mod1 * mod2 * mod3

        # Calcul des dégâts
        degats = int(
            (
                (
                    (
                        (
                            (
                                (self.niveau_attaquant * 2 / 5) + 2
                            ) * self.puissance * att_attaquant / 50
                        ) / def_adversaire
                    ) * modificateur
                ) + 2
            ) * r / 100
        )

        # Appliquer les dégâts
        adversaire.statistiques.points_de_vie -= degats

        print(f"{attaquant.nom} utilise {self.nom} et inflige {degats} dégâts à {adversaire.nom}")
        print(f"Type Capacité: {self.type_capacite}")
        print(f"Type Adversaire: {adversaire.type}")

# Exemple d'instanciation d'une capacité
Charge = Capacite("Charge", 40, 100, 35, "Normal", "Physique")
Rugissement = Capacite("Rugissement", 0, 100, 40, "Normal", "Statut", {'statistique': 'Attaque'})
Mimi_Queue = Capacite("Mimi-Queue", 0, 100, 30, "Normal", "Statut", {'statistique': 'Defense'})
Flammèche = Capacite("Flammèche", 40, 100, 25, "Feu", "Spéciale")
Pistolet_a_O = Capacite("Pistolet à O", 40, 100, 25, "Eau", "Spéciale")
Fouet_Lianes = Capacite("Fouet Lianes", 40, 100, 25, "Plante", "Spéciale")
