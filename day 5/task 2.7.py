pokemon = input("pokemon: ")
types = {
    "Electric": ["Pikachu"],
    "Grass": ["Bulbasaur", "Leafeaon"],
    "Fire": ["Charmander", "Scovillain"]
}

for pokemon_type in types:
    if pokemon in types[pokemon_type]:
        print(pokemon_type)