#!/bin/python

import sys
import inspect
from random import *

from fighter import *
from items.items import Potion
from items.items import Sirop
from skills import Tourment


class Enemy(Fighter):
    # def __init__(self, name, hp, atk, pwr, pr, mr, exp =None, loot =None, skills =None):
    def __init__(self, name, stats=None, loot=None, skills=None):
        Fighter.__init__(self, name, stats, loot, skills)

    ### ???
    ### OVERRIDE METHODS :
    ### TO REDEFINE IN ENEMY CLASSES
    ### ???
    def choose_turn(self):
        # action = random()
        action = 0.1
        if action < 0.5:  # attack
            return self.attack
        elif action < 0.8:  # skill
            return self.cast_skill
        return self.use_item  # item

    def fight_turn(self, foe):
        # choose_turn return fonction action
        action = self.choose_turn()
        if action == self.attack:
            action(foe)
        print foe.hp

    ###
    ### GENERIC METHODS :
    ### COMMON FOR ALL ENEMIES
    ###

    ### ITEM FUNCS
    def use_item(self):
        item = choice(self.items)
        item.use(self)

    def reward(self):
        if self.items:
            return choice(self.items)  # Item object
        return None

    ### SKILL FUNCS
    def cast_skill(self):
        skill = choice(self.skills.keys())
        skill.cast()


###
### ENEMY CLASSES
###

class Soul(Enemy):
    name = 'soul'
    stats = {
        'HP': 20,
        'ATK': 2,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 10
    }
    items = [Potion, Sirop]
    skills = [Tourment]

    # For instances & function (Instances useless ? => go static functions ?)
    def __init__(self, name =name, stats =stats, items =items, skills =skills):
        Enemy.__init__(self, name, stats, items, skills)

class Specter(Enemy):
    name = 'specter'
    stats = {
        'HP': 8,
        'ATK': 4,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 10
    }
    items = [Potion]
    skills = [Tourment]

    # For instances & function (Instances useless ? => go static functions ?)
    def __init__(self, name=name, stats=stats, items=items, skills=skills):
        Enemy.__init__(self, name, stats, items, skills)


def fill_enemy_classes():
    enemy_list = []
    # name = Soul, obj = enemies.Soul
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        print name, obj
        if obj.__module__ == __name__ and name != 'Enemy':
            enemy_list.append(obj)
    return enemy_list


enemy_classes = fill_enemy_classes()
