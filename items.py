#!/bin/python


###########################
###   EFFECT FUNCS      ###
###   SEPARATE MODULE ? ###
###########################


# ATTENTION : si target = enemy, no missing_hp() (TODO: faire une classe Fighter, parent commun de Hero, Enemy)
def gain_hp(target, hp =0):
    hero = target
    try:
        if target.hp == target.stats['HP']:
            print "No need to use this : FULL HP"
            return False
        if target.missing_hp() < hp:
            target.hp = target.stats['HP']
        else:
            target.hp += hp
        print "%s\nHP : %i / %i" % (target.name, target.hp, target.stats['HP'])
        return True
    except ValueError:
        print "Glob.hero undefined"


#######################
###   ITEM FUNCS    ###
#######################

def use_potion(target):
    return gain_hp(target, hp=5)



###########################
###  ITEM=>FUNC TABLES  ###
###########################

use_item_func = {
    'potion': use_potion,
    'sirop': 2
}

equip_item_func = {
    'amulette': 2
}

craft_item_func = {
    'croc': 1,
    'poil': 1
}


'''
class Item:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect

potion = Item('potion', 'common', ['hp', '+', '20'])
sirop = Item('sirop', 'common', ['mp', '+', '40'])
amulette = Item('amulette', 'common', ['mr', '+', '10'])
croc = Item('croc', 'common', ['atk', '+', '5'])
poil = Item('poil', 'frequent', [])
'''