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
#####   #####   items.py         calls adapted to changes below, TEST:print_enemy_classes()
#####   #####   init_game.py    calls adapted to changes below
#####   #####   world.py        calls adapted to changes below, include enemies (instead of enemy_data)
#####   #####   fights.py       CHANGE:fight(hero, enemy)
#####   #####   enemy_data.py   CHANGE:name.lower() => MERGED with enemies.py
#####   #####   enemies.py      ADD:choose_turn(), ADD:cast_skill(), ADD:enemy_classes = fill_enemy_classes() [CRITICAL]
#####   #####   hero.py         calls adapted to changes below, MOVE:missing_hp() -> fighter.py
#####   #####   fighter.py      CHANGE:self.items, ADD:->missing_hp()
#####   #####   skills.py       CHANGE:name.lower, CHANGE:table = {Obj: level}
"""
from console_ui import print_hero_inventaire, print_hero_skills, print_pokedex, print_hero_info, print_enemy
from enemies import Soul
from fights import fight
from init_game import init
from printer import Printer
from variables import Glob
from world import glob_travel
from world import write_world

# TESTS better

init()
#
# success = 0
# for i in range(0, 50):
#     spawn, enemy = Glob.current_place.spawn_enemy()
#     if spawn:
#         success += 1
# print str(success) + "/50"

print "You are in " + Glob.current_place.name

# for e in enemy_classes:
#     print e.name

Glob.current_place = Glob.current_place.child_list[0]
# spawn, enemy = Glob.current_place.spawn_enemy()
# while not spawn:
#     spawn, enemy = Glob.current_place.spawn_enemy()
# fight(Glob.hero, enemy())

while True:
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
        try:
            print_enemy(Glob.pokedex[enemy_name])
        except KeyError:
            Printer.err("%s was not in my pokedex..." % enemy_name)
    if 'item' in cmd or 'items' in cmd:
        print_hero_inventaire()
    if 'use' in cmd:
        print_hero_inventaire()
        item_name = raw_input("What item to use ? ")
        Glob.hero.use_item(item_name)
        # Glob.current_place.spawn_enemy()
    if 'cast' in cmd:
        print_hero_skills()
        skill_name = raw_input("What spell to cast ? ")
        Glob.hero.cast_skill(skill_name)
        # Glob.current_place.spawn_enemy()

'''
print "GAME START !"
while MAIN_LOOP:
    for event in pygame.event.get():
        if event.type ==
    draw_game(Glob.current_place, Glob.hero) #call pygame.display.update()
'''
