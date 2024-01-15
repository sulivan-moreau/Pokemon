import pygame
import sys
import random
import time
from PIL import Image
from Capacité import *
from Type_Pokemon import types_pokemon

# Initialisation de Pygame
pygame.init()

# Définir les couleurs
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)

# Définir la fenêtre (variable globale)
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Choisissez votre Pokémon")

# Redimensionner les images des Pokémon
def redimensionner_image(image_path, nouvelle_taille):
    img = Image.open(image_path)
    img_resized = img.resize(nouvelle_taille)
    nouveau_chemin = f"resized_{image_path}"
    img_resized.save(nouveau_chemin)
    return pygame.image.load(nouveau_chemin)

# Charger les images des Pokémon
image_feu = redimensionner_image("autocollant-salameche-pokemon-004.png", (200, 200))
image_eau = redimensionner_image("250px-Carapuce-RFVF.png", (200, 200))
image_plante = redimensionner_image("autocollant-bulbizarre-pokemon-001.png", (200, 200))

# Classe pour les statistiques du Pokémon
class Statistiques:
    def __init__(self):
        self.attaque = random.randint(1, 15)
        self.defense = random.randint(1, 15)
        self.attaque_speciale = random.randint(1, 15)
        self.defense_speciale = random.randint(1, 15)
        self.vitesse = random.randint(1, 15)
        self.points_de_vie = 20

def calculer_degats(attaque, defense, type_attaquant, type_defenseur):
    # ... logique pour calculer les dégâts ...
    # Utilise les relations entre les types pour ajuster les dégâts
    # Pour l'exemple, renvoyons simplement une valeur aléatoire
    return random.randint(1, 10)

# Classe de base pour les Pokémon
class Pokemon:
    def __init__(self, nom, type_pokemon, image, capacites):
        self.nom = nom
        self.type = type_pokemon
        self.image = image
        self.statistiques = Statistiques()
        self.capacites = capacites

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
            ("Attaque", self.statistiques.attaque),
            ("Défense", self.statistiques.defense),
            ("Attaque Spéciale", self.statistiques.attaque_speciale),
            ("Défense Spéciale", self.statistiques.defense_speciale),
            ("Vitesse", self.statistiques.vitesse),
        ]

        pygame.draw.rect(fenetre, NOIR, (x, y, 200, 150))
        for i, (attribut, valeur) in enumerate(attributs):
            texte_attribut = font.render(f"{attribut}: {valeur}", True, BLANC)  # Utiliser BLANC ici
            fenetre.blit(texte_attribut, (x + 5, y + i * 30 + 5))

    def attaquer(self, adversaire):
        degats = calculer_degats(
            self.statistiques.attaque,
            adversaire.statistiques.defense,
            self.type,
            adversaire.type
        )
        adversaire.statistiques.points_de_vie -= degats
        print(f"{self.nom} inflige {degats} dégâts à {adversaire.nom}")

    def utiliser(self, adversaire):
        # Sélectionnez une capacité au hasard parmi celles du Pokémon
        capacite_choisie = random.choice(self.capacites)

        # Appel de la méthode utiliser de la capacité sélectionnée
        degats = capacite_choisie.utiliser(self, adversaire)

        print(f"{self.nom} utilise {capacite_choisie.nom} et inflige {degats} dégâts à {adversaire.nom}")

# Classes spécifiques pour chaque type de Pokémon
class PokemonFeu(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Feu", image, capacites)

class PokemonEau(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Eau", image, capacites)

class PokemonPlante(Pokemon):
    def __init__(self, nom, image, capacites):
        super().__init__(nom, "Plante", image, capacites)

class GameManager:
    def __init__(self):
        self.pokemon_choisi = None
        self.adversaire = None

    def choisir_pokemon(self):
        pokemons = [
            PokemonFeu("Salamèche", image_feu, ["Rugissement", "Charge", "Flammèche"]),
            PokemonEau("Carapuce", image_eau, ["Rugissement" , "Charge", "Pistolet à  O"]),
            PokemonPlante("Bulbizarre", image_plante, ["Mimi Queue" , "Charge", "Fouet Lianes"])
        ]

        choix = 0  # Indice du Pokémon sélectionné
        x_position = 50  # Position x de l'affichage des Pokémon

        selection_effectuee = False

        en_cours = True
        while en_cours:
            fenetre.fill(NOIR)  # Fond noir

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        choix = (choix - 1) % 3
                    elif event.key == pygame.K_RIGHT:
                        choix = (choix + 1) % 3
                    elif event.key == pygame.K_SPACE:
                        if not selection_effectuee :
                                selection_effectuee = True
                                en_cours = False

            # Afficher les Pokémon et leurs statistiques
            for i, pokemon in enumerate(pokemons):
                pokemon_x = x_position + i * (200 + 50)
                pokemon.afficher_image(pokemon_x, 200)
                pokemon.afficher_statistiques(pokemon_x, 170)

            pokemons[choix].afficher_details(0, 0)

            # Mettre en surbrillance le Pokémon sélectionné
            pygame.draw.rect(fenetre, ROUGE, (x_position + choix * (200 + 50), 200, 200, 200), 2)

            pygame.display.flip()

        return pokemons[choix]

class CombatManager:
    def __init__(self, pokemon_joueur, pokemon_adversaire):
        self.pokemon_joueur = pokemon_joueur
        self.pokemon_adversaire = pokemon_adversaire
        self.attaque_selectionnee = None

    def afficher_menu_attaques(self):
        font = pygame.font.Font(None, 36)
        attaques = self.pokemon_joueur.capacites

        for i, attaque in enumerate(attaques):
            texte_attaque = font.render(f"{i + 1}. {attaque}", True, BLANC)
            capacite_attaque = self.pokemon_joueur.capacites[i]

            fenetre.blit(texte_attaque, (50, 400 + i * 30))

    def combat(self):
        while self.pokemon_joueur.statistiques.points_de_vie > 0 and self.pokemon_adversaire.statistiques.points_de_vie > 0:
            # Afficher les informations sur le combat
            print(f"{self.pokemon_joueur.nom} - PV: {self.pokemon_joueur.statistiques.points_de_vie}")
            print(f"{self.pokemon_adversaire.nom} - PV: {self.pokemon_adversaire.statistiques.points_de_vie}")

            # Attaque du joueur
            if self.attaque_selectionnee is not None and 0 <= self.attaque_selectionnee < len(self.pokemon_joueur.capacites):
                capacite_joueur = self.pokemon_joueur.capacites[self.attaque_selectionnee]
                degats_joueur = capacite_joueur.utiliser(self.pokemon_joueur, self.pokemon_adversaire)
                print(f"{self.pokemon_joueur.nom} utilise {capacite_joueur.nom} et inflige {degats_joueur} dégâts.")
                time.sleep(1)  # Ajouter un délai d'une seconde

            if self.pokemon_adversaire.statistiques.points_de_vie <= 0:
                print(f"{self.pokemon_joueur.nom} a gagné !")
                break

            # Attaque de l'adversaire
            capacite_adversaire = random.choice(self.pokemon_adversaire.capacites)
            degats_adversaire = capacite_adversaire.utiliser(self.pokemon_adversaire, self.pokemon_joueur)
            print(f"{self.pokemon_adversaire.nom} utilise {capacite_adversaire.nom} et inflige {degats_adversaire} dégâts.")
            time.sleep(1)  # Ajouter un délai d'une seconde

            if self.pokemon_joueur.statistiques.points_de_vie <= 0:
                print(f"{self.pokemon_adversaire.nom} a gagné !")
                break

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
                            # Exécutez l'attaque sélectionnée
                            self.pokemon_joueur.attaquer(self.pokemon_adversaire)
                            self.attaque_selectionnee = None
                            self.combat()
                            en_cours = False
                    elif event.key in [pygame.K_1, pygame.K_2]:
                        # Sélectionnez une attaque en fonction du chiffre
                        self.attaque_selectionnee = int(event.unicode) - 1

            fenetre.fill(NOIR)  # Fond noir

            self.pokemon_joueur.afficher_image(50, 200)
            self.pokemon_joueur.afficher_statistiques(50, 170)
            self.pokemon_adversaire.afficher_image(largeur - 250, 200)
            self.pokemon_adversaire.afficher_statistiques(largeur - 250, 170)

            if self.attaque_selectionnee is not None:
                pygame.draw.rect(fenetre, ROUGE, (50, 400 + self.attaque_selectionnee * 30, 200, 30), 2)

            self.afficher_menu_attaques()

            pygame.display.flip()

if __name__ == "__main__":
    game_manager = CombatManager(None, None)
    game_manager.main()
