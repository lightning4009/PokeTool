class BattleItem:

    def __init__(self, item_name, item_type, boosts_move_power, boosts_stat, boosts_type, heals, reduces_type, boost_factor, heal_factor, type_reduced, types_boosted, stats_boosted, criteria):
        self.name = item_name
        self.item_type = item_type
        self.boosts_move_power = boosts_move_power
        self.boosts_stat = boosts_stat
        self.boosts_type = boosts_type
        self.heals = heals
        self.reduces_type = reduces_type
        self.boost_factor = boost_factor
        self.heal_factor = heal_factor
        self.type_reduced = type_reduced
        self.types_boosted = types_boosted
        self.stats_boosted = stats_boosted
        self.criteria = criteria
    
    def __str__(self):
        return self.name


filename = 'battle_items.csv'

battle_item_dex = {}

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
        if line[2] == 'TRUE':
            boosts_move_power = True
        else:
            boosts_move_power = False

        if line[3] == 'TRUE':
            boosts_stat = True
        else:
            boosts_stat = False

        if line[4] == 'TRUE':
            boosts_type = True
        else:
            boosts_type = False

        if line[5] == 'TRUE':
            heals = True
        else:
            heals = False

        if line[6] == 'TRUE':
            reduces_type = True
        else:
            reduces_type = False
        
        boost_factor = line[7]
        heal_factor = line[8]
        type_reduced = line[9]

        types_boosted = []

        boosted_types_list = line[10].split(':')
        for item in boosted_types_list:
            types_boosted.append(item)

        stats_boosted = []
        
        stats_boosted_list = line[11].split(':')
        for item in stats_boosted_list:
            stats_boosted.append(item)
        
        criteria = line[12]
        
        battle_item = BattleItem(item_name, item_type, boosts_move_power, boosts_stat, boosts_type, heals, reduces_type, boost_factor, heal_factor, type_reduced, types_boosted, stats_boosted, criteria)

        battle_item_dex[item_name] = battle_item
        
    
    file_object.close()
