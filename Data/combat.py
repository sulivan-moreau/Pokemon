import random
import json

def load_pokemon(pokeedex.json):
    with open(pokeedex.json, "r") as file:
        pokedex = json.load(file)

    def get_pokemon_by_name(name):
        for pokemon_name, pokemon_data in pokedex.items():
            if pokemon_name.lower() == name.lower():
                return Pokemon(**pokemon_data)
        return None

    return get_pokemon_by_name

class Pokemon:
    def __init__(self, name, type, defense, attack, level):
        self.name = name
        self.type = type
        self.defense = defense
        self.attack = attack
        self.level = level
        self.hp = 100

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Niveau: {self.level}, PV: {self.hp}, Attaque: {self.attack}, Défense: {self.defense})"

class Combat:
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player_pokemon = player_pokemon
        self.enemy_pokemon = enemy_pokemon

    def attack(self):
        damage = self.player_pokemon.attack * self.get_damage_multiplier(self.player_pokemon.type, self.enemy_pokemon.type)
        self.enemy_pokemon.hp -= damage
        return f"{self.player_pokemon.name} attaque {self.enemy_pokemon.name} avec {damage} dégâts !"

    def defense(self):
        damage_reduction = self.enemy_pokemon.attack * self.get_damage_multiplier(self.enemy_pokemon.type, self.player_pokemon.type)
        self.player_pokemon.hp -= damage_reduction
        return f"{self.enemy_pokemon.name} attaque {self.player_pokemon.name} avec {damage_reduction} dégâts !"

    def get_damage_multiplier(self, attacker_type, defender_type):
        damage_multiplier = 1
        if attacker_type == defender_type:
            damage_multiplier = 0.5
        elif attacker_type == "feu" and defender_type == "eau":
            damage_multiplier = 2
        elif attacker_type == "eau" and defender_type == "feu":
            damage_multiplier = 0.5
        elif attacker_type == "plante" and defender_type == "feu":
            damage_multiplier = 2
        elif attacker_type == "feu" and defender_type == "plante":
            damage_multiplier = 0.5
        elif attacker_type == "plante" and defender_type == "eau":
            damage_multiplier = 1
        elif attacker_type == "eau" and defender_type == "plante":
            damage_multiplier = 0.5
        elif attacker_type == "plante" and defender_type == "plante":
            damage_multiplier = 1
        elif attacker_type == "plante" and defender_type == "feu":
            damage_multiplier = 1
        elif attacker_type == "feu" and defender_type == "plante":
            damage_multiplier = 2
        return damage_multiplier

    def check_winner(self):
        if self.player_pokemon.hp <= 0:
            return f"{self.enemy_pokemon.name} a gagné le combat !"
        elif self.enemy_pokemon.hp <= 0:
            return f"{self.player_pokemon.name} a gagné le combat !"
        else:
            return "Match nul !"

    def start_combat(self):
        while self.player_pokemon.hp > 0 and self.enemy_pokemon.hp > 0:
            print(self.attack())
            if self.enemy_pokemon.hp > 0:
                print(self.defense())
            else:
                break
        return self.check_winner()

def load_pokemon(file_name):
    with open(file_name, "r")