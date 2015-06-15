#!/bin/python

import effects
from named import Named

# TODO : various checks (global table)


#######################
###   CLASSES       ###
#######################

class Skill(Named):
    def __init__(self, text=''):
        if text == '':
            text = '- %i %s' % (self.value, self.stat)
        self.text = text

#######################
###  SKILL CLASSES  ###
#######################
class Tourment(Skill):
    value = 5
    stat = 'HP'

    @staticmethod
    def cast(stat):
        new_stat = effects.loose_stat(stat, Tourment.value)
        return new_stat

    @staticmethod
    def castskill(target=None, val=value, t=stat):
        if effects.deal_dmg(target, dmg=val):
            print t
            return True
        return False

class Cri(Skill):
    value = 3
    stat = 'HP'

    @staticmethod
    def cast(stat):
        new_stat = effects.loose_stat(stat, Tourment.value)
        return new_stat

    @staticmethod
    def castskill(target=None, val=value, t=stat):
        if effects.deal_dmg(target, dmg=val):
            print t
            return True
        return False
###########################
###  SKILL=>NAME TABLES ###
###########################
# skill_table = {
#     Tourment: 1
# }
# 'Cri': 1,
# 'Morsure': 5,
#     'Charge': 5,
#     'Fireball': 10,
#     'Iceball': 10,
#     'Energy Shot': 15
#
# }
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
