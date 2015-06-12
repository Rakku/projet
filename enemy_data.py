#!/bin/python


# import Gameplay data :
# class Module {}
# items = Module(...)
from enemies import *


class Soul(Enemy):
    name = 'Soul'
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
    def __init__(self, name=name, stats=stats, items=items, skills=skills):
        Enemy.__init__(self, name, stats, items, skills)


class Specter(Enemy):
    name = 'Specter'
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


'''
items = {
    'Soul': [Potion, Sirop],
    'Specter': [Potion]
    #'Wolf': ['croc', 'poil']
}

skills = {
    'Soul': [Tourment],
    'Specter': [Tourment]
    #'Wolf': ['Morsure', 'Charge']
}

base_stats = {
    'Soul': {
        'HP': 20,
        'ATK': 2,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 10
    },
    'Specter': {
        'HP': 20,
        'ATK': 5,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 10
    },
    'Wolf': {
        'HP': 20,
        'ATK': 5,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 10
    }
}
'''
