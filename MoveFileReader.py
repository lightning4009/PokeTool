from Types import TYPES
from Pokemon import Move

filename = 'moves.csv'

move_dex = {}
attack_dex = {}

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
        
        move_id = int(line[0])
        move_name = line[1]
        move_type = TYPES[line[2]]
        move_category = line[3]
        move_power = int(line[4])
        move_damage_type = line[5]
        if line[6] == 'no':
            has_secondary_effect = False
        else:
            has_secondary_effect = True
            
        if line[7] == 'no':
            makes_contact = False
        else:
            makes_contact = True
        
        if line[8] == 'no':
            is_multihit = False
        else:
            is_multihit = True
            
        max_no_hits = line[9]
        
        move = Move(move_id, move_name, move_type, move_category, move_power, move_damage_type, has_secondary_effect, makes_contact, is_multihit, max_no_hits)
        move_dex[move.move_id] = move
        
        if move.category != 'Status':
            attack_dex[move.name] = move
    
    file_object.close()