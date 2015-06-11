#!/bin/python


# import Gameplay data :
# class Module {}
# items = Module(...)
from skills import *
from items import *



enemy_items = {
    'Soul': ['potion', 'sirop'],
    'Specter': ['amulette'],
    'Wolf': ['croc', 'poil']
}

enemy_skills = {
    'Soul': ['Tourment'],
    'Specter': ['Tourment', 'Cri'],
    'Wolf': ['Morsure', 'Charge']
}

enemy_base_stats = {
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