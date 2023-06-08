from Types import TYPES
from Pokemon import Pokemon
from Pokemon import Pokedex

filename = 'pokemon.csv'

dex = Pokedex()

try:
    with open(filename) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    pass
else:
    del lines[0]
    for line in lines:
        line = line.strip()
        line = line.split(',')
        
        id_num = int(line[0])
        dex_num = int(line[1])
        region = line[2]
        name = line[3]
        types = {'type1': TYPES[line[4]], 'type2': TYPES[line[5]]}
        abilities = {'ability1': line[6], 'ability2': line[7], 'h_ability': line[8]}
        stats = {'hp': int(line[9]), 'atk': int(line[10]), 'def': int(line[11]), 'spatk': int(line[12]), 'spdef': int(line[13]), 'spd': int(line[14])}
        weight = float(line[16])
        height = float(line[17])
        
        
        pokemon = Pokemon(id_num, dex_num, region, name, types, abilities, stats, weight, height)
        dex.AddPokemon(pokemon)
    
    file_object.close()