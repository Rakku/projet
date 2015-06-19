#!/bin/python

import sys
import inspect
from random import *

from load import load_items, load_skills
from fighter import *
from load import my_import


# TODO : Tests (see Hero)
class Enemy(Fighter):
    def __init__(self, stats=None, loot=None, skills=None):
        Fighter.__init__(self, stats, loot, skills)

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
        # action = self.choose_turn()
        # if action == self.attack:
        #    action(foe)
        self.attack(foe)

    ### ITEM FUNCS
    def use_item(self):
        item = my_import('items.items', choice(self.items.keys()))
        item.use(self.stats, self.max_stats)

    def reward(self):
        gain = choice(self.items.keys())  # Item object
        return gain

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
    items = {"Potion": 1, "Sirop": 5}
    skills = {"Tourment": 1}

    # For instances & function (Instances useless ? => go static functions ?)
    def __init__(self, stats=stats, items=items, skills=skills):
        #items = load_items(items) # TODO
        #skills = load_skills(skills) # TODO
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
    items = {"Potion": 1}
    skills = {"Tourment": 1}

    # For instances & function (Instances useless ? => go static functions ?)
    def __init__(self, stats=stats, items=items, skills=skills):
        #items = load_items(items) # TODO
        #skills = load_skills(skills) # TODO
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
