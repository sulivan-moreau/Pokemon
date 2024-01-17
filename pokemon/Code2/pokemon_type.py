class TypePokemon:
    def __init__(self, nom):
        self.nom = nom
        self.relations = {}

# Initialisation des types
types_pokemon = {
    "Normal": TypePokemon("Normal"),
    "Feu": TypePokemon("Feu"),
    "Plante": TypePokemon("Plante"),
    "Eau": TypePokemon("Eau"),
    "Roche": TypePokemon("Roche"),
    "Combat": TypePokemon("Combat"),
    "Insecte": TypePokemon("Insecte"),
    "Poison": TypePokemon("Poison"),
    "Acier": TypePokemon("Acier"),
    "Électrik": TypePokemon("Électrik"),
    "Psy": TypePokemon("Psy"),
    "Ténèbres": TypePokemon("Ténèbres"),
    "Spectre": TypePokemon("Spectre"),
    "Dragon": TypePokemon("Dragon"),
    "Glace": TypePokemon("Glace"),
    "Fée": TypePokemon("Fée"),
    "Vol": TypePokemon("Vol"),
    "Sol": TypePokemon("Sol"),
}

# Relations d'avantage/désavantage pour chaque type
types_pokemon["Eau"].relations = {
    "Normal":1, "Feu": 2, "Acier": 1, "Eau": 0.5, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 0.5, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol": 2, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 2
}

types_pokemon["Feu"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 2, "Eau": 0.5, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 2, "Glace": 2, "Insecte": 2,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 0.5
}

types_pokemon["Plante"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 2, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 0.5, "Glace": 1, "Insecte": 0.5,
    "Poison": 0.5, "Psy": 1, "Sol": 2, "Spectre": 1, "Ténèbres": 1, "Vol": 0.5, "Roche": 2
}

types_pokemon["Normal"].relations = {
 
    "Normal":1, "Feu": 1, "Acier": 0.5, "Eau": 1, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 0, "Ténèbres": 1, "Vol": 1, "Roche": 0.5
}

types_pokemon["Acier"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 0.5, "Dragon": 0.5, "Combat": 1,
    "Fée": 2, "Électrik": 0.5, "Plante": 1, "Glace": 2, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 2
}

types_pokemon["Combat"].relations = {

    "Normal":0.5, "Feu": 1, "Acier": 2, "Eau": 1, "Dragon": 0.5, "Combat": 1,
    "Fée": 0.5, "Électrik": 1, "Plante": 1, "Glace": 2, "Insecte": 0.5,
    "Poison": 0.5, "Psy": 0.5, "Sol": 1, "Spectre": 1, "Ténèbres": 2, "Vol": 0.5, "Roche": 2
}

types_pokemon["Dragon"].relations = {

    "Normal":1, "Feu": 1, "Acier": 0.5, "Eau": 1, "Dragon": 2, "Combat": 1,
    "Fée": 0, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 1
}

types_pokemon["Électrik"].relations = {

    "Normal":1, "Feu": 1, "Acier": 1, "Eau": 2, "Dragon": 0.5, "Combat": 1,
    "Fée": 1, "Électrik": 0.5, "Plante": 0.5, "Glace": 1, "Insecte": 0.5,
    "Poison": 1, "Psy": 1, "Sol": 0, "Spectre": 1, "Ténèbres": 1, "Vol": 2, "Roche": 1
}

types_pokemon["Fée"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 1, "Dragon": 2, "Combat": 2,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 0.5, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 2, "Vol": 1, "Roche": 1
}

types_pokemon["Psy"].relations = {

    "Normal":1, "Feu": 1, "Acier": 0.5, "Eau": 1, "Dragon": 1, "Combat": 2,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 2, "Psy": 0.5, "Sol": 1, "Spectre": 1, "Ténèbres": 0, "Vol": 1, "Roche": 1
}

types_pokemon["Glace"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 0.5, "Dragon": 2, "Combat": 0.5,
    "Fée": 1, "Électrik": 1, "Plante": 2, "Glace": 0.5, "Insecte": 1,
    "Poison": 1, "Psy": 1, "Sol":2, "Spectre": 1, "Ténèbres": 2, "Vol": 2, "Roche": 1
}

types_pokemon["Poison"].relations = {

    "Normal":1, "Feu": 1, "Acier": 0, "Eau": 1, "Dragon": 1, "Combat": 2,
    "Fée": 2, "Électrik": 1, "Plante": 2, "Glace": 1, "Insecte": 1,
    "Poison": 0.5, "Psy": 1, "Sol": 0.5, "Spectre": 0.5, "Ténèbres": 1, "Vol": 1, "Roche": 0.5
}

types_pokemon["Roche"].relations = {

    "Normal":1, "Feu": 2, "Acier": 0.5, "Eau": 1, "Dragon": 1, "Combat": 0.5,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 2, "Insecte": 2,
    "Poison": 1, "Psy": 1, "Sol": 0.5, "Spectre": 1, "Ténèbres": 1, "Vol": 2, "Roche": 1
}

types_pokemon["Sol"].relations = {

    "Normal":1, "Feu": 2, "Acier": 2, "Eau": 1, "Dragon": 1, "Combat": 1,
    "Fée": 1, "Électrik": 2, "Plante": 0.5, "Glace": 0.5, "Insecte": 1,
    "Poison": 2, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 0, "Roche": 2
}

types_pokemon["Spectre"].relations = {

    "Normal":0, "Feu": 1, "Acier": 1, "Eau": 1, "Dragon": 1, "Combat": 1,
    "Fée": 1, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 2, "Sol": 1, "Spectre": 2, "Ténèbres": 0.5, "Vol": 1, "Roche": 1
}

types_pokemon["Ténèbres"].relations = {

    "Normal":1, "Feu": 1, "Acier": 1, "Eau": 1, "Dragon": 1, "Combat": 0.5,
    "Fée": 0.5, "Électrik": 1, "Plante": 1, "Glace": 1, "Insecte": 1,
    "Poison": 1, "Psy": 2, "Sol": 1, "Spectre": 2, "Ténèbres": 0.5, "Vol": 1, "Roche": 1
}

types_pokemon["Vol"].relations = {

    "Normal":1, "Feu": 1, "Acier": 0.5, "Eau": 1, "Dragon": 1, "Combat": 2,
    "Fée": 1, "Électrik": 0.5, "Plante": 2, "Glace": 1, "Insecte": 2,
    "Poison": 1, "Psy": 1, "Sol": 1, "Spectre": 1, "Ténèbres": 1, "Vol": 1, "Roche": 0.5
}

types_pokemon["Insecte"].relations = {

    "Normal":1, "Feu": 0.5, "Acier": 0.5, "Eau": 1, "Dragon": 1, "Combat": 0.5,
    "Fée": 0.5, "Électrik": 1, "Plante": 2, "Glace": 1, "Insecte": 1,
    "Poison": 0.5, "Psy": 2, "Sol": 1, "Spectre": 0.5, "Ténèbres": 2, "Vol": 0.5, "Roche": 0.5
}