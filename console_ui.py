#!/bin/python

#######################
###   CONSOLE PRINTING
###   LIB OF STANDALONE FUNCS
###   ONLY NEED GLOBALS
#######################

from variables import Glob

class Action:
    def __init__(self, name, func):
        self.name = name
        self.action = func
        self.text = ''

def get_string(obj_tab):
    str = ""
    for elt in obj_tab:
        str += "%s " % elt.name
    return str

#######################
###   MAPS          ###
#######################

# Not ready for testing
def print_map():
    node = Glob.current_place
    for x in range(0, node.size):
        str = '.'
        for y in range(0, node.size):
            if Glob.hero.pos[0] == x and Glob.hero.pos[1] == y:
                str += "X."
            else:
                str += "_."

def print_travel():
    len = Glob.current_place.child_list.__len__()

    print "You are now in " + Glob.current_place.name
    print "Where to go ?"
    if not Glob.current_place.parent is None:
        print "--- %s ---" % str(Glob.current_place.parent.__class__)
        print "0 " + Glob.current_place.parent.name
    print "--- %s ---" % str(Glob.current_place.child_list[0].__class__)
    for i in range(0, len):
        print str(i+1) + " " + Glob.current_place.child_list[i].name

#######################
###   INFOS         ###
#######################

###
###   HEROS
###

### STATS

def print_hero_stats():
    hero = Glob.hero
    print " --> Stats :"
    print "HP : %i / %i" % (hero.hp, hero.stats['HP'])
    print "ATK : %i" % hero.atk
    print "PWR : %i" % hero.pwr
    print "RES : %i" % hero.res
    print "MR : %i" % hero.mr
    print "EXP : %i" % hero.exp

### ITEMS
'''
def print_hero_usables():
    if a in Glob.hero.items
'''

def print_hero_inventaire():
    inv = ""
    for key in Glob.hero.items:
        if Glob.hero.items[key] > 0:
            inv += "%s x%i " % (key.name, Glob.hero.items[key])
    print " --> Inventaire :"
    print inv
    return inv

### SKILLS

def print_hero_skills():
    str = ""
    for elt in Glob.hero.skills:
        str += "%s " % elt.name
    print " --> Skills :"
    print str
    return str

def print_hero_info():
    print " %s : %s Niv. %i" % (Glob.hero.name, Glob.hero.spec, Glob.hero.level)
    print_hero_stats()
    print_hero_inventaire()
    print_hero_skills()

###
###   ENEMY
###

def print_enemy(enemy):
    print "--- " + enemy.name
    for stat in enemy.stats:
        print stat + " = " + str(enemy.stats[stat])
    gain = ""
    for item in enemy.items:
        gain += "%s " % item
    #gain = get_string(enemy.loot)
    print "Can drop : %s" % gain

def print_pokedex():
    pokedex = Glob.pokedex
    for key in pokedex:
        print pokedex[key].name

#######################
###   FIGHTS        ###
#######################

def print_fight_choices():
    i = 0
    hero = Glob.hero
    i += 1
    print "%i Attack" % i
    if hero.skills:
        i += 1
        print "%i Skill" % i
    if hero.items:
        i += 1
        print "%i Items" % i

def print_enemy_killed(enemy, gain):
    print "You have killed %s !" % enemy.name
    print "You gain %i EXP" % enemy.exp
    if gain:
        print "You have looted %s !" % gain.name
