import random 
from pokemon_type import types_pokemon

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

    def evaluer_efficacite(self, adversaire):
        type_attaque = self.type_capacite
        type_adversaire = adversaire.type[0].lower()

        if len(adversaire.type) == 2:
            type_adversaire = adversaire.type[1].lower()

        effectiveness = types_pokemon[type_attaque].relations.get(type_adversaire, 1.0)

        if effectiveness == 2:
            print(f"L'attaque est super efficace !")
        elif effectiveness == 1:
            print(f"L'attaque est efficace")
        elif effectiveness == 0.5:
            print(f"L'attaque n'est pas très efficace.")
        elif effectiveness == 0:
            print(f"L'attaque n'a aucun effet.")

            # Phrase sur le pourcentage de baisse de statistique
            if self.effet_statistique:
                pourcentage_baisse = self.effet_statistique.get('pourcentage', 0)
                print(f"L'attaque de {adversaire.nom} baisse de {pourcentage_baisse}%.")

    def utiliser(self, attaquant, adversaire):
        # Détermination si l'attaque est physique ou spéciale
        if self.classe_capacite == "Physique":
            att_attaquant = attaquant.statistiques.attaque
            def_adversaire = adversaire.statistiques.defense
        else:
            att_attaquant = attaquant.statistiques.attaque_speciale
            def_adversaire = adversaire.statistiques.defense_speciale

        # Coup critique
        coup_critique = 2 if random.randint(1, 100) <= 10 else 1  # 10% de chance de coup critique

        # Calcul du modificateur aléatoire R
        r = random.choice([i for i in range(85, 100)] * 2 + [100]) / 255.0

        # STAB
        stab = 2 if self.type_capacite in attaquant.type else 1

        # Type de l'attaque par rapport aux types du défenseur
        type1_multiplier = types_pokemon[self.type_capacite.lower()].relations.get(adversaire.type[0].lower(), 1.0)

        if len(adversaire.type) == 2:
            type2_multiplier = types_pokemon[self.type_capacite.lower()].relations.get(adversaire.type[1].lower(), 1.0)


        # Calcul des dégâts selon la formule
        degats = int(
            (
                (
                    (
                        (
                            (
                                (attaquant.niveau * 2 / 5) + 2
                            ) * self.puissance * att_attaquant / 50
                        ) / def_adversaire
                    ) * coup_critique * r / 100
                ) + 2
            ) * stab * type1_multiplier * type2_multiplier
        )

        # Dégâts minimum de 1 si le défenseur n'est pas immunisé
        degats = max(degats, 1)

        # Appliquer les dégâts
        adversaire.statistiques.points_de_vie -= degats

        print(f"{attaquant.nom} utilise {self.nom}.")
        print(f"{adversaire.nom} a perdu {degats} PV.")

        self.evaluer_efficacite(adversaire)

        return degats, self.effet_statistique

# Exemple d'instanciation d'une capacité
Charge = Capacite("Charge", 40, 100, 35, "Normal", "Physique")
Rugissement = Capacite("Rugissement", 0, 100, 40, "Normal", "Statut", {'statistique': 'Attaque'})
Mimi_Queue = Capacite("Mimi-Queue", 0, 100, 30, "Normal", "Statut", {'statistique': 'Defense'})
Flammèche = Capacite("Flammèche", 40, 100, 25, "Feu", "Spéciale")
Pistolet_a_O = Capacite("Pistolet à O", 40, 100, 25, "Eau", "Spéciale")
Fouet_Lianes = Capacite("Fouet Lianes", 40, 100, 25, "Plante", "Spéciale")
