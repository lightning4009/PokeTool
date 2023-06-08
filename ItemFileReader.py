class Item:

    def __init__(self, item_name, item_type, in_battle_effect, out_of_battle_effect, fling_damage, can_be_flung):
        self.name = item_name
        self.item_type = item_type
        self.in_battle_effect = in_battle_effect
        self.out_of_battle_effect = out_of_battle_effect
        self.fling_damage = fling_damage
        self.can_be_flung = can_be_flung
    
    def __str__(self):
        return self.item_name + ' ' + self.in_battle_effect + ' and ' + self.out_of_battle_effect


filename = 'items.csv'

item_dex = {}

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
        
        item_name = line[0]
        item_type = line[1]
        in_battle_effect = line[2]
        out_of_battle_effect = line[3]
        fling_damage = int(line[4])
        can_be_flung = line[5]
        
        item = Item(item_name, item_type, in_battle_effect, out_of_battle_effect, fling_damage, can_be_flung)

        item_dex[item_name] = item
        
    
    file_object.close()
