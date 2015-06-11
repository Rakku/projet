#!/bin/python

'''
#####   VERSION : ALPHA
#####   UI : CONSOLE
#####   #####   COMMANDS : MOVE ZONE HERO ENEMY USE CAST
#####   #####   MAPS :
#####   #####   #####   Castlevania > Castle 1
#####   #####   #####   Boktai > Solaria > First
#####   #####   #####   Zelda > Hyrule > Boutique
                              > Kokiri

#####   TODO : OBJECTS ITEM & SKILL + METHODS
'''

from init_game import *
from world import *
from enemies import *
from hero import *
import re

init()

success = 0
for i in range(0,50):
    spawn, enemy = Glob.current_place.spawn_enemy()
    if spawn:
        success += 1
print str(success) + "/50"


print "You are in " + Glob.current_place.name


while(1):
    cmd = raw_input()
    action = cmd.split()
    if 'move' in cmd:
        glob_travel()
    if 'zone' in cmd:
        print "You are in " + Glob.current_place.name
        write_world(Glob.current_place)
    if 'hero' in cmd:
        print_hero_info()
    if 'enemy' in cmd:
        print_pokedex()
        enemy_name = raw_input("What enemy to study ? ")
        print_enemy(Glob.pokedex[enemy_name])
    if 'item' in cmd or 'items' in cmd:
        print_hero_inventaire()
    if 'use' in cmd:
        print_hero_inventaire()
        item_name = raw_input("What item to use ? ")
        Glob.hero.use_item(item_name)
    if 'cast' in cmd:
        print_hero_skills()
        skill_name = raw_input("What spell to cast ? ")
        Glob.hero.cast_skill(skill_name)


'''
print "GAME START !"
while MAIN_LOOP:
    for event in pygame.event.get():
        if event.type ==
    draw_game(Glob.current_place, Glob.hero) #call pygame.display.update()
'''