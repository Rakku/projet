#!/bin/python


#import effects
from named import Named

# TODO : various checks (global table)


#######################
###   CLASSES       ###
#######################

class Skill(Named):
    stat_effects = {
        'HP': -5,
        'ATK': -1
        # 'PWR': 0,
        # 'RES': 0,
        # 'MR': 0,
        # 'EXP': 0
    }

    def __init__(self, stats=stat_effects, text=''):
        self.effects = stats
        if text == '':
            for stat in self.effects:
                if self.effects[stat] != 0:
                    text = '- %i %s\n' % (self.effects[stat], stat)
        self.text = text

    def cast(self, stats):
        for stat in self.effects:
            stats[stat] += self.effects[stat]

#######################
###  SKILL CLASSES  ###
#######################


class Tourment(Skill):
    stat_effects = {'HP': -5}

    def __init__(self, effects=stat_effects):
        Skill.__init__(self, effects)


class Cri(Skill):
    stat_effects = {'RES': -1}

    def __init__(self, effects=stat_effects):
        Skill.__init__(self, effects)
###########################
###  SKILL=>NAME TABLES ###
###########################
#
#
# class Skill:
#     def __init__(self, name, dmg, descr):
#         self.name = name
#         self.dmg = dmg
#         self.descr = descr
#
# tourment = Skill('Tourment', 2, 'Leave me!')
# cri = Skill('Cri', 1, 'Kiyaa!')
# morsure = Skill('Morsure', 5, 'Peste!')
# charge = Skill('Charge', 5, 'Here I Come')
#
# fireball = Skill('Fireball', 10, 'It burns')
# iceball = Skill('Iceball', 10, 'It freezes')
# energyshot = Skill('Energy Shot', 15, 'It hurts')
