import Pokemon

class Nature:
    def __init__(self, id, name, raised_stat, lowered_stat, liked_flavor, disliked_flavor):
        self.id = id
        self.name = name
        self.raised_stat = raised_stat
        self.lowered_stat = lowered_stat
        self.liked_flavor = liked_flavor
        self.disliked_flavor = disliked_flavor

    def __str__(self):
        return str(self.id) + ': ' + self.name + '\nRaises: ' + self.raised_stat + '\nLowers: ' + self.lowered_stat + '\nLikes: ' + self.liked_flavor + '\nDislikes: ' + self.disliked_flavor 

filename = 'natures.csv'

NATURES = {}

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
        name = line[1]
        increased_stat = line[2]
        decreased_stat = line[3]
        fav_flav = line[4]
        disliked_flav = line[5]
        
        
        nature = Nature(id_num, name, increased_stat, decreased_stat, fav_flav, disliked_flav)
        NATURES[name] = nature
    
    file_object.close()