import Pokemon
import PySimpleGUI as psg
import tkinter as tk

from PokemonFileReader import dex
from MoveFileReader import move_dex
from MoveFileReader import attack_dex
from NatureFileReader import NATURES
from Types import TYPES
from ItemFileReader import item_dex
from BattleItemFileReader import battle_item_dex

#goodra = Pokemon.Pokemon(706, 'Kalos', 'Goodra', {'type1': 'dragon', 'type2': 'none'}, {'ability1': 'Gooey', 'ability2': 'Hydration', 'h_ability': 'Sap Sipper'}, {'hp': 90, 'atk': 100, 'def': 70, 'spatk': 110, 'spdef': 150, 'spd': 80})
#goomy = Pokemon.Pokemon(705, 'Kalos', 'Goomy', {'type1': 'dragon', 'type2': 'none'}, {'ability1': 'Gooey', 'ability2': 'Hydration', 'h_ability': 'Sap Sipper'}, {'hp': 45, 'atk': 50, 'def': 35, 'spatk': 55, 'spdef': 75, 'spd': 40})
#print(f'{goomy} \n {goodra}')

#print(Pokemon.CalcHp(goodra, 100))
#print(Pokemon.CalcStat(goodra, 'atk', 100))

#test = ((((2 * goodra.stats['atk'] + 31 + (0//4)) * 100)//100)) + 5

#print (test)



#dex.AddPokemon(goomy)
#dex.AddPokemon(goodra)

#print(dex)

#print(dex.GetPokemon(999)[1])
#print(dex.GetPokemon(706)[0].height)

#print(dex.GetPokemon(706)[0].types['type1'].CheckDefensiveRelationship(dex.GetPokemon(700)[0].types['type1']))

#if dex.GetPokemon(706)[0].types['type1'].name in Pokemon.TYPES:
    #print (Pokemon.TYPES[dex.GetPokemon(706)[0].types['type1'].name])
#else:
    
    #print('no')

#print(dex.GetPokemonNames(706))

stat_ivs = {'hp': 31, 'atk': 31, 'def': 31, 'spatk': 31, 'spdef': 31, 'spd': 31}
stat_evs = {'hp': 248, 'atk': 0, 'def': 0, 'spatk': 252, 'spdef': 8, 'spd': 0}

stat_ivs2 = {'hp': 31, 'atk': 31, 'def': 31, 'spatk': 31, 'spdef': 31, 'spd': 31}
stat_evs2 = {'hp': 0, 'atk': 0, 'def': 0, 'spatk': 252, 'spdef': 4, 'spd': 252}

stat_ivs3 = {'hp': 31, 'atk': 31, 'def': 31, 'spatk': 31, 'spdef': 31, 'spd': 31}
stat_evs3 = {'hp': 0, 'atk': 252, 'def': 0, 'spatk': 0, 'spdef': 4, 'spd': 252}

#print(Pokemon.CalcAllStats(dex.GetPokemon(706)[0], 100, stat_ivs, stat_evs))
#print(Pokemon.CalcAllStats(goomy, 100, stat_ivs, stat_evs))

battle_goo = Pokemon.BattlePokemon(dex.GetPokemon(706)[0], TYPES['dragon'], 100, stat_ivs, stat_evs, NATURES['Modest'], dex.GetPokemon(706)[0].abilities['ability1'], battle_item_dex['Dragon Gem'], 'none')
battle_typh = Pokemon.BattlePokemon(dex.GetPokemon(157)[0], TYPES['fire'], 100, stat_ivs2, stat_evs2, NATURES['Timid'], dex.GetPokemon(157)[0].abilities['ability1'], battle_item_dex['Fire Gem'], 'none')
battle_prim = Pokemon.BattlePokemon(dex.GetPokemon(730)[0], TYPES['water'], 100, stat_ivs, stat_evs, NATURES['Modest'], dex.GetPokemon(730)[0].abilities['ability1'], battle_item_dex['Fairy Gem'], 'none')
battle_rai = Pokemon.BattlePokemon(dex.GetPokemon(26)[2], TYPES['electric'], 100, stat_ivs2, stat_evs2, NATURES['Timid'], dex.GetPokemon(26)[2].abilities['ability1'], battle_item_dex['Electric Gem'], 'none')
battle_sand = Pokemon.BattlePokemon(dex.GetPokemon(28)[1], TYPES['ice'], 100, stat_ivs3, stat_evs3, NATURES['Adamant'], dex.GetPokemon(28)[1].abilities['ability1'], battle_item_dex['Ice Gem'], 'none')
battle_lud = Pokemon.BattlePokemon(dex.GetPokemon(272)[0], TYPES['grass'], 100, stat_ivs2, stat_evs2, NATURES['Timid'], dex.GetPokemon(272)[0].abilities['ability1'], battle_item_dex['Water Gem'], 'none')

#Damage Calc Tests#

#Neutral, not boosted by weather, STAB#
test = battle_goo.CalculateDamage(battle_typh, attack_dex['Draco Meteor'], 'none')

#Resisted 1x, not boosted by weather, STAB#
test2 = battle_prim.CalculateDamage(battle_typh, attack_dex['Moonblast'], 'sun')

#Resisted 2x, not boosted by weather, STAB#
test3 = battle_sand.CalculateDamage(battle_sand, attack_dex['Icicle Crash'], 'none')

#Super effective 1x, not boosted by weather, STAB#
test4 = battle_prim.CalculateDamage(battle_goo, attack_dex['Moonblast'], 'rain')

#Super effective 2x, not boosted by weather, STAB#
test5 = battle_typh.CalculateDamage(battle_sand, attack_dex['Eruption'], 'none')

#Neutral, not boosted by weather, not STAB#
test6 = battle_typh.CalculateDamage(battle_rai, attack_dex['Solar Beam'], 'none')

#Resisted 1x, not boosted by weather, not STAB#
test7 = battle_typh.CalculateDamage(battle_goo, attack_dex['Solar Beam'], 'none')

#Resisted 2x, not boosted by weather, not STAB#
test8 = battle_prim.CalculateDamage(battle_sand, attack_dex['Ice Beam'], 'none')

#Super effective 1x, not boosted by weather, not STAB#
test9 = battle_typh.CalculateDamage(battle_prim, attack_dex['Solar Beam'], 'none')

#Super effective 2x, not boosted by weather, not STAB#
test10 = battle_goo.CalculateDamage(battle_sand, attack_dex['Flamethrower'], 'none')



#Neutral, boosted by weather, STAB#
test11 = battle_typh.CalculateDamage(battle_rai, attack_dex['Eruption'], 'sun')

#Resisted 1x, boosted by weather, STAB#
test12 = battle_typh.CalculateDamage(battle_goo, attack_dex['Eruption'], 'sun')

#Resisted 2x, boosted by weather, STAB#
test13 = battle_prim.CalculateDamage(battle_lud, attack_dex['Hydro Pump'], 'rain')

#Super effective 1x, boosted by weather, STAB#
test14 = battle_prim.CalculateDamage(battle_typh, attack_dex['Hydro Pump'], 'rain')

#Super effective 2x, boosted by weather, STAB#
test15 = battle_typh.CalculateDamage(battle_sand, attack_dex['Eruption'], 'sun')

#Neutral, boosted by weather, not STAB#
test16 = battle_goo.CalculateDamage(battle_lud, attack_dex['Flamethrower'], 'sun')

#Resisted 1x, boosted by weather, not STAB#
test17 = battle_goo.CalculateDamage(battle_prim, attack_dex['Flamethrower'], 'sun')

#Resisted 2x, boosted by weather, not STAB#
test18 = battle_goo.CalculateDamage(battle_lud, attack_dex['Aqua Tail'], 'rain')

#Super effective 1x, boosted by weather, not STAB#
test19 = battle_goo.CalculateDamage(battle_typh, attack_dex['Aqua Tail'], 'rain')

#Super effective 2x, boosted by weather, not STAB#
test20 = battle_goo.CalculateDamage(battle_sand, attack_dex['Flamethrower'], 'sun')



#Neutral, weakened by weather, STAB#
test21 = battle_typh.CalculateDamage(battle_rai, attack_dex['Eruption'], 'rain')

#Resisted 1x, weakened by weather, STAB#
test22 = battle_typh.CalculateDamage(battle_prim, attack_dex['Eruption'], 'rain')

#Resisted 2x, weakened by weather, STAB#
test23 = battle_prim.CalculateDamage(battle_lud, attack_dex['Hydro Pump'], 'sun')

#Super effective 1x, weakened by weather, STAB#
test24 = battle_prim.CalculateDamage(battle_typh, attack_dex['Hydro Pump'], 'sun')

#Super effective 2x, weakened by weather, STAB#
test25 = battle_typh.CalculateDamage(battle_sand, attack_dex['Eruption'], 'rain')

#Neutral, weakened by weather, not STAB#
test26 = battle_goo.CalculateDamage(battle_lud, attack_dex['Flamethrower'], 'rain')

#Resisted 1x, weakened by weather, not STAB#
test27 = battle_goo.CalculateDamage(battle_prim, attack_dex['Flamethrower'], 'rain')

#Resisted 2x, weakened by weather, not STAB#
test28 = battle_goo.CalculateDamage(battle_lud, attack_dex['Aqua Tail'], 'sun')

#Super effective 1x, weakened by weather, not STAB#
test29 = battle_goo.CalculateDamage(battle_typh, attack_dex['Aqua Tail'], 'sun')

#Super effective 2x, weakened by weather, not STAB#
test30 = battle_goo.CalculateDamage(battle_sand, attack_dex['Flamethrower'], 'rain')



#Immune#
test31 = battle_goo.CalculateDamage(battle_prim, attack_dex['Draco Meteor'], 'none')

print(battle_prim.stats)

for value in test:
    print(f't1 {value}')
print ('\n')
for value in test2:
    print(f't2 {value}')
print('\n')
for value in test3:
    print(f't3 {value}')
print('\n')
for value in test4:
    print(f't4 {value}')
print('\n')
for value in test5:
    print(f't5 {value}')
print('\n')
for value in test6:
    print(f't6 {value}')
print('\n')
for value in test7:
    print(f't7 {value}')
print('\n')
for value in test8:
    print(f't8 {value}')
print('\n')
for value in test9:
    print(f't9 {value}')
print('\n')
for value in test10:
    print(f't10 {value}')
print('\n')
for value in test11:
    print(f't11 {value}')
print('\n')
for value in test12:
    print(f't12 {value}')
print('\n')
for value in test13:
    print(f't13 {value}')
print('\n')
for value in test14:
    print(f't14 {value}')
print('\n')
for value in test15:
    print(f't15 {value}')
print('\n')
for value in test16:
    print(f't16 {value}')
print('\n')
for value in test17:
    print(f't17 {value}')
print('\n')
for value in test18:
    print(f't18 {value}')
print('\n')
for value in test19:
    print(f't19 {value}')
print('\n')
for value in test20:
    print(f't20 {value}')
print('\n')
for value in test21:
    print(f't21 {value}')
print('\n')
for value in test22:
    print(f't22 {value}')
print('\n')
for value in test23:
    print(f't23 {value}')
print('\n')
for value in test24:
    print(f't24 {value}')
print('\n')
for value in test25:
    print(f't25 {value}')
print('\n')
for value in test26:
    print(f't26 {value}')
print('\n')
for value in test27:
    print(f't27 {value}')
print('\n')
for value in test28:
    print(f't28 {value}')
print('\n')
for value in test29:
    print(f't29 {value}')
print('\n')
for value in test30:
    print(f't30 {value}')
print('\n')
for value in test31:
    print(f't31 {value}')

battle_goo.ChangeMove('move1', move_dex[406])
print(battle_goo)


#layout = [[psg.Text(text='Hello World',
#                    font=('Arial Bold', 20),
#                    size=20,
#                    expand_x=True,
#                    justification='center')],
#          ]

#window = psg.Window('HelloWorld', layout, size=(715,250))

#while True:
#    event, values = window.read()
#    print(event, values)
#    if event in(None, 'Exit'):
#        break
#window.close()