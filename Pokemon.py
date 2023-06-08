import BattleItemFileReader

class Pokemon:
    
    def __init__(self, id_num, dex_num, region, name, types, abilities, stats, weight, height):
        self.id_num = id_num
        self.dex_num = dex_num
        self.region = region
        self.name = name
        self.types = types
        self.abilities = abilities
        self.stats = stats
        self.bst = int(stats['hp']) + int(stats['atk']) + int(stats['def']) + int(stats['spatk']) + int(stats['spdef']) + int(stats['spd'])
        self.height = height
        self.weight = weight
    
    def __str__(self):
        return 'Pokemon #' + str(self.dex_num) + ': ' + self.name + '\nType: ' + self.types['type1'].name + '/' + self.types['type2'].name + '\nRegion: ' + self.region + '\nAbilities: ' + self.abilities['ability1'] + '\t' + self.abilities['ability2'] + '\t' + self.abilities['h_ability'] + '\n\nHP: ' + str(self.stats['hp']) + '\nAttack: ' + str(self.stats['atk']) + '\nDefense: ' + str(self.stats['def']) + '\nSpecial Attack: ' + str(self.stats['spatk']) + '\nSpecial Defense: ' + str(self.stats['spdef']) + '\nSpeed: ' + str(self.stats['spd']) + '\nBase Stat Total: ' + str(self.bst)

class Pokedex:
    
    def __init__(self):
        self.pokemon_list = {}
    
    def AddPokemon(self, pokemon):
        if not self.CheckDexNum(pokemon):
            self.pokemon_list[pokemon.dex_num] = [pokemon]
        else:
            self.pokemon_list[pokemon.dex_num].append(pokemon)
        
    def CheckDexNum(self, pokemon):
        if pokemon.dex_num in self.pokemon_list:
            return True
        else:
            return False
        
    def GetPokemon(self, dex_num):

        return self.pokemon_list[dex_num]
    
    def GetPokemonNames(self, dex_num):
        
        return_string = ''
        
        for pokemon in self.pokemon_list[dex_num]:
            return_string += pokemon.name + '\n'
        
        return return_string
    
    def __str__(self):
        dexString = ''
        for pokemon in self.pokemon_list:
            dexString += str(pokemon) + ': ' + self.GetPokemonNames(pokemon) + '\n'
        return dexString
    
class BattlePokemon:
    
    def __init__(self, pokemon, tera_type, level, ivs, evs, nature, ability, item, status):
        self.pokemon = pokemon
        self.tera_type = tera_type
        self.level = level
        self.ivs = ivs
        self.evs = evs
        self.nature = nature
        self.ability = ability
        self.item = item
        self.moves = {'move1': '', 'move2': '', 'move3': '', 'move4': ''}
        self.status = status
        self.stats = {}
        
    def CalcHp(self):    
        step1 = (2 * self.pokemon.stats['hp'])
        step2 = step1 + self.ivs['hp']
        step3 = self.evs['hp']//4
        step4 = step2 + step3
        step5 = step4 * self.level
        step6 = step5//100
        step7 = step6 + self.level
        realHp = step7 + 10
        
        return realHp

    def CalcStat(self, stat):
        
        step1 = (2 * self.pokemon.stats[stat])
        step2 = step1 + self.ivs[stat]
        step3 = self.evs[stat]//4
        step4 = step2 + step3
        step5 = step4 * self.level
        step6 = step5//100
        realStat = step6 + 5

        if self.nature.raised_stat == stat:
            
            realStat = int(realStat * 1.1)
        
        elif self.nature.lowered_stat == stat:
            realStat = int(realStat * .9)
        
        return realStat

    def CalcAllStats(self):
    
        real_stats = {}
    
        for iv in self.ivs:
            if iv == 'hp':
                real_stats[iv] = self.CalcHp()
            else:
                real_stats[iv] = self.CalcStat(iv)
    
        return real_stats
    
    def ChangeMove(self, move_to_change, new_move):
        self.moves[move_to_change] = new_move
    
    
    def UpdateStats(self):
        self.stats = self.CalcAllStats()

    def StabBoost(self, attack, damage_range):
        return_range = []
        if attack.attack_type in self.pokemon.types.values():
            for value in damage_range:
                return_range.append(PokeRound(value * (6144/4096)))
            return return_range
        else:
            return damage_range
    
    def TypeEffectiveness(self, attack, opposing_pokemon):
        type_effectiveness = 1

        for p_type in opposing_pokemon.pokemon.types.values():
            type_effectiveness *= attack.attack_type.CheckOffensiveRelationship(p_type)

        return type_effectiveness
        
    
    def CalculateDamage(self, opposing_pokemon, attack, weather):
        
        self.UpdateStats()
        opposing_pokemon.UpdateStats()
        base_damage = 0
        move_base_power = attack.power
        random_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        damage_range = []
        stab_damage_range = []
        final_damage_range = []
        item_damage_range = []

        if self.item.name in BattleItemFileReader.battle_item_dex:
            print('item yes')
            print(self.item.boosts_type)
            if self.item.boosts_type and self.item.criteria == '-':
                print('boost yes')
                if attack.attack_type.name in self.item.types_boosted:
                    boost_factor = self.item.boost_factor
                    boost_factor_arr = boost_factor.split('/')
                    move_base_power = PokeRound(move_base_power * int(boost_factor_arr[0])/int(boost_factor_arr[1]))

        step1 = 2 * self.level
        step2 = (step1//5) + 2
        step3 = step2 * move_base_power

        
        if attack.category == 'Physical':
            
            step4 = step3 * self.stats['atk']
            step5 = step4 // opposing_pokemon.stats['def']
        elif attack.category == 'Special':
            
            step4 = step3 * self.stats['spatk']
            step5 = step4 // opposing_pokemon.stats['spdef']       

        step6 = step5 // 50
        base_damage = step6 + 2
    
        
        if weather == 'sun' and attack.attack_type.name == 'fire':
            base_damage = PokeRound(base_damage * 6144/4096)
        elif weather == 'sun' and attack.attack_type.name == 'water':
            base_damage = PokeRound(base_damage * 2048/4096)
        elif weather == 'rain' and attack.attack_type.name == 'fire':
            base_damage = PokeRound(base_damage * 2048/4096)
        elif weather == 'rain' and attack.attack_type.name == 'water':
            base_damage = PokeRound(base_damage * 6144/4096)
        elif weather == 'sandstorm' and 'rock' in opposing_pokemon.pokemon.types.values() and attack.category == 'Special':
            base_damage = PokeRound(base_damage * 2048/4096)
        elif weather == 'snow' and 'ice' in opposing_pokemon.pokemon.types.values() and attack.category == "Physical":
            base_damage = PokeRound(base_damage * 2048/4096)
        
                
        for value in random_range:
            s1 = 100 - value
            s2 = s1 * base_damage
            s3 = s2 // 100
            damage_range.append(s3)


        stab_damage_range = self.StabBoost(attack, damage_range)
        
        for value in stab_damage_range:
            final_damage_range.append(int(value * self.TypeEffectiveness(attack, opposing_pokemon)))

        return final_damage_range
    
    def __str__(self):
        return self.pokemon.name + ' ' + self.tera_type.name + ' ' + str(self.level) + ' ' + self.nature.name + ' ' + self.moves['move1'].name
        
        
    
class Move:
    
    def __init__(self, move_id,  name, attack_type, category, power, damage_type, secondary_effect, contact, multihit, max_number_of_hits):
        self.move_id = move_id
        self.name = name
        self.attack_type = attack_type
        self.category = category
        self.power = power
        self.damage_type = damage_type
        self.has_secondary_effect = secondary_effect
        self.makes_contact = contact
        self.is_multihit = multihit
        self.max_number_of_hits = max_number_of_hits
        
    def __str__(self):
        return self.name + '\nType: ' + self.attack_type.name + '\nPower: ' + str(self.power)
    
    
class PokemonType:
    
    def __init__(self, name, weak_to, resistant_against, immune_to, super_effective_against, not_very_effective_against, innefective_against):
        self.name = name
        self.weak_to = weak_to
        self.resistant_against = resistant_against
        self.immune_to = immune_to
        self.super_effective_against = super_effective_against
        self.not_very_effective_against = not_very_effective_against
        self.innefective_against = innefective_against
    
    def CheckDefensiveRelationship(self, attacking_type):
        if attacking_type.name in self.weak_to:
            return 2
        elif attacking_type.name in self.resistant_against:
            return .5
        elif attacking_type.name in self.immune_to:
            return 0
        else:
            return 1
        
    def CheckOffensiveRelationship(self, defending_type):
        if defending_type.name in self.super_effective_against:
            return 2
        elif defending_type.name in self.not_very_effective_against:
            return .5
        elif defending_type.name in self.innefective_against:
            return 0
        else:
            return 1
    
    def __str__(self):
        return self.name



def PokeRound(value):
    if value % 1 > .5:
        return int(value) + 1
    else:
        return int(value)
    
def Round(value):
    if value % 1 >= .5:
        return int(value) + 1
    else:
        return int(value)