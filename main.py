#!/bin/python

"""
#####   VERSION : ALPHA
#####   UI : CONSOLE
#####   #####   COMMANDS : MOVE ZONE HERO ENEMY USE CAST
#####   #####   MAPS :
#####   #####   #####   Castlevania > Castle 1
#####   #####   #####   Boktai > Solaria > First
#####   #####   #####   Zelda > Hyrule > Boutique
                              > Kokiri

#####   TODO : OBJECT LOOTING (map), SKILL LEARNING, MERGE ENEMIES + ENEMY_DATA

#####   USEFUL : if hasattr(obj, 'attribute') [ better try + except ]

#####   DIFF FILES (8) :
#####   #####   main.py         calls adapted to changes below, TEST:print_enemy_classes()
#####   #####   init_game.py    calls adapted to changes below
#####   #####   world.py        calls adapted to changes below, include enemies (instead of enemy_data)
#####   #####   fights.py       CHANGE:fight(hero, enemy)
#####   #####   enemy_data.py   CHANGE:name.lower() => MERGED with enemies.py
#####   #####   enemies.py      ADD:choose_turn(), ADD:cast_skill(), ADD:enemy_classes = fill_enemy_classes() [CRITICAL]
#####   #####   hero.py         calls adapted to changes below, MOVE:missing_hp() -> fighter.py
#####   #####   fighter.py      CHANGE:self.items, ADD:->missing_hp()
#####   #####   skills.py       CHANGE:name.lower, CHANGE:table = {Obj: level}
"""

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

for e in enemy_classes:
    print e.name

fight(Glob.hero, Soul())

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
        enemy_name = raw_input("What enemy to study ? ").lower()
        print_enemy(Glob.pokedex[enemy_name])
    if 'item' in cmd or 'items' in cmd:
        print_hero_inventaire()
    if 'use' in cmd:
        print_hero_inventaire()
        item_name = raw_input("What item to use ? ").lower()
        Glob.hero.use_item(item_name)
        Glob.current_place.spawn_enemy()
    if 'cast' in cmd:
        print_hero_skills()
        skill_name = raw_input("What spell to cast ? ").lower()
        Glob.hero.cast_skill(skill_name)
        Glob.current_place.spawn_enemy()


'''
print "GAME START !"
while MAIN_LOOP:
    for event in pygame.event.get():
        if event.type ==
    draw_game(Glob.current_place, Glob.hero) #call pygame.display.update()
'''