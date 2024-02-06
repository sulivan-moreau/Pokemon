class TypePokemon:
    def __init__(self, nom):
        self.nom = nom
        self.relations = {}

    # Initialisation des types
types_pokemon = {
    "normal": TypePokemon("Normal"),
    "feu": TypePokemon("Feu"),
    "plante": TypePokemon("Plante"),
    "eau": TypePokemon("Eau"),
    "roche": TypePokemon("Roche"),
    "combat": TypePokemon("Combat"),
    "insecte": TypePokemon("Insecte"),
    "poison": TypePokemon("Poison"),
    "acier": TypePokemon("Acier"),
    "électrik": TypePokemon("Électrik"),
    "psy": TypePokemon("Psy"),
    "ténèbres": TypePokemon("Ténèbres"),
    "spectre": TypePokemon("Spectre"),
    "dragon": TypePokemon("Dragon"),
    "glace": TypePokemon("Glace"),
    "fée": TypePokemon("Fée"),
    "vol": TypePokemon("Vol"),
    "sol": TypePokemon("Sol"),
}

# Relations d'avantage/désavantage pour chaque type
types_pokemon["eau"].relations = {
"normal": 1, "feu": 2, "acier": 1, "eau": 0.5, "dragon": 0.5, "combat": 1,
"fée": 1, "électrik": 1, "plante": 0.5, "glace": 1, "insecte": 1,
"poison": 1, "psy": 1, "sol": 2, "spectre": 1, "ténèbres": 1, "vol": 1, "roche": 2
}

types_pokemon["feu"].relations = {
"normal": 1, "feu": 0.5, "acier": 2, "eau": 0.5, "dragon": 0.5, "combat": 1,
"fée": 1, "électrik": 1, "plante": 2, "glace": 2, "insecte": 2,
"poison": 1, "psy": 1, "sol": 1, "spectre": 1, "ténèbres": 1, "vol": 1, "roche": 0.5
}

types_pokemon["plante"].relations = {
"normal": 1, "feu": 0.5, "acier": 0.5, "eau": 2, "dragon": 0.5, "combat": 1,
"fée": 1, "électrik": 1, "plante": 0.5, "glace": 1, "insecte": 0.5,
"poison": 0.5, "psy": 1, "sol": 2, "spectre": 1, "ténèbres": 1, "vol": 0.5, "roche": 2
}

types_pokemon["normal"].relations = {
"normal": 1, "feu": 1, "acier": 0.5, "eau": 1, "dragon": 0.5, "combat": 1,
"fée": 1, "électrik": 1, "plante": 1, "glace": 1, "insecte": 1,
"poison": 1, "psy": 1, "sol": 1, "spectre": 0, "ténèbres": 1, "vol": 1, "roche": 0.5
}

types_pokemon["acier"].relations = {
"normal": 1, "feu": 0.5, "acier": 0.5, "eau": 0.5, "dragon": 0.5, "combat": 1,
"fée": 2, "électrik": 0.5, "plante": 1, "glace": 2, "insecte": 1,
"poison": 1, "psy": 1, "sol": 1, "spectre": 1, "ténèbres": 1, "vol": 1, "roche": 2
}

types_pokemon["combat"].relations = {
"normal": 0.5, "feu": 1, "acier": 2, "eau": 1, "dragon": 0.5, "combat": 1,
"fée": 0.5, "électrik": 1, "plante": 1, "glace": 2, "insecte": 0.5,
"poison": 0.5, "psy": 0.5, "sol": 1, "spectre": 1, "ténèbres": 2, "vol": 0.5, "roche": 2
}

types_pokemon["dragon"].relations = {
"normal": 1, "feu": 1, "acier": 0.5, "eau": 1, "dragon": 2, "combat": 1,
"fée": 0, "électrik": 1, "plante": 1, "glace": 1, "insecte": 1,
"poison": 1, "psy": 1, "sol": 1, "spectre": 1, "ténèbres": 1, "vol": 1, "roche": 1
}

types_pokemon["électrik"].relations = {
"normal": 1, "feu": 1, "acier": 1, "eau": 2, "dragon": 0.5, "combat": 1,
"fée": 1, "électrik": 0.5, "plante": 0.5, "glace": 1, "insecte": 0.5,
"poison": 1, "psy": 1, "sol": 0, "spectre": 1, "ténèbres": 1, "vol": 2, "roche": 1
}

types_pokemon["fée"].relations = {
"normal": 1, "feu": 0.5, "acier": 0.5, "eau": 1, "dragon": 2, "combat": 2,
"fée": 1, "électrik": 1, "plante": 1, "glace": 1, "insecte": 1,
"poison": 0.5, "psy": 1, "sol": 1, "spectre": 1, "ténèbres": 2, "vol": 1, "roche": 1
}

types_pokemon["psy"].relations = {
"normal": 1, "feu": 1, "acier": 0.5, "eau": 1, "dragon": 1, "combat": 2,
"fée": 1, "électrik": 1, "plante": 1, "glace": 1, "insecte": 1,
"poison": 2, "psy": 0.5, "sol": 1, "spectre": 1, "ténèbres": 0, "vol": 1, "roche": 1
}

types_pokemon["glace"].relations = {
"normal": 1, "feu": 0.5, "acier": 0.5, "eau": 0.5, "dragon": 2, "combat": 0.5,
"fée": 1, "électrik": 1, "plante": 2, "glace": 0.5, "insecte": 1,
"poison": 1, "psy": 1, "sol": 2, "spectre": 1, "ténèbres": 2, "vol": 2, "roche": 1
}

types_pokemon["poison"].relations = {
"normal": 1, "feu": 1, "acier": 0, "eau": 1, "dragon": 1, "combat": 2,
"fée": 2, "électrik": 1, "plante": 2, "glace": 1, "insecte": 1,
"poison": 0.5, "psy": 1, "sol": 0.5, "spectre": 0.5, "ténèbres": 1, "vol": 1, "roche": 0.5
}

types_pokemon["roche"].relations = {
"normal": 1, "feu": 2, "acier": 0.5, "eau": 1, "dragon": 1, "combat": 0.5,
"fée": 1, "électrik": 1, "plante": 1, "glace": 2, "insecte": 2,
"poison": 1, "psy": 1, "sol": 0.5, "spectre": 1, "ténèbres": 1, "vol": 2, "roche": 1
}

types_pokemon["sol"].relations = {
"normal": 1, "feu": 2, "acier": 2, "eau": 1, "dragon": 1, "combat": 1,
"fée": 1, "électrik": 2, "plante": 0.5, "glace": 0.5, "insecte": 1,
"poison": 2, "psy": 1, "sol": 1, "spectre": 1, "ténèbres": 1, "vol": 0, "roche": 2
}

types_pokemon["spectre"].relations = {
"normal": 0, "feu": 1, "acier": 1, "eau": 1, "dragon": 1, "combat": 1,
"fée": 1, "électrik": 1, "plante": 1, "glace": 1, "insecte": 1,
"poison": 1, "psy": 2, "sol": 1, "spectre": 2, "ténèbres": 0.5, "vol": 1, "roche": 1
}

types_pokemon["ténèbres"].relations = {
"normal": 1, "feu": 1, "acier": 1, "eau": 1, "dragon": 1, "combat": 0.5,
"fée": 0.5, "électrik": 1, "plante": 1, "glace": 1, "insecte": 1,
"poison": 1, "psy": 2, "sol": 1, "spectre": 2, "ténèbres": 0.5, "vol": 1, "roche": 1
}

types_pokemon["vol"].relations = {
"normal": 1, "feu": 1, "acier": 0.5, "eau": 1, "dragon": 1, "combat": 2,
"fée": 1, "électrik": 0.5, "plante": 2, "glace": 1, "insecte": 2,
"poison": 1, "psy": 1, "sol": 1, "spectre": 1, "ténèbres": 1, "vol": 1, "roche": 0.5
}

types_pokemon["insecte"].relations = {
"normal": 1, "feu": 0.5, "acier": 0.5, "eau": 1, "dragon": 1, "combat": 0.5,
"fée": 0.5, "électrik": 1, "plante": 2, "glace": 1, "insecte": 1,
"poison": 0.5, "psy": 2, "sol": 1, "spectre": 0.5, "ténèbres": 2, "vol": 0.5, "roche": 0.5
}
