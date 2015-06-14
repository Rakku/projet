#!/bin/python

import sys
import inspect
from random import *

from load import load_items, load_skills
from fighter import *


# TODO : Tests (see Hero)
class Enemy(Fighter):
    # def __init__(self, name, hp, atk, pwr, pr, mr, exp =None, loot =None, skills =None):
    def __init__(self, stats=None, loot=None, skills=None):
        Fighter.__init__(self, stats, loot, skills)



    # @staticmethod
    # def load_enemy_skills(skills):
    #     new_skills = []
    #     for skil in skills:
    #         # __import__()
    #         pass  # TODO: Remove (the pass is here to avoid a Syntax error :))
    #         # clazz = my_import('skills.' + item) # TODO: Code a method to import a class dynamically
    #         # obj = clazz()
    #         # new_items.append(obj)
    #     return new_skills

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
    stats = {
        'HP': 20,
        'ATK': 2,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 10
    }
    items = ["Potion", "Sirop"] # TODO: Use strings instead of useless dependencies
    # items = [Potion, Sirop]
    skills = ["Tourment"]

    # For instances & function (Instances useless ? => go static functions ?)
    def __init__(self, stats=stats, items=items, skills=skills):
        items = load_items(items) # TODO
        skills = load_skills(skills) # TODO
        Enemy.__init__(self, stats, items, skills)


class Specter(Enemy):
    stats = {
        'HP': 8,
        'ATK': 4,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 10
    }
    items = ["Potion"]
    skills = ["Tourment"]

    # For instances & function (Instances useless ? => go static functions ?)
    def __init__(self, stats=stats, items=items, skills=skills):
        items = load_items(items) # TODO
        skills = load_skills(skills) # TODO
        Enemy.__init__(self, stats, items, skills)




def fill_enemy_classes():
    enemy_list = []
    # name = Soul, obj = enemies.Soul
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        print name, obj
        if obj.__module__ == __name__ and name != 'Enemy':
            enemy_list.append(name)
    return enemy_list


enemy_classes = fill_enemy_classes()
