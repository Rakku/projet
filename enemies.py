#!/bin/python

from random import *
from fighter import *
from enemy_data import *



class Enemy(Fighter):
    #def __init__(self, name, hp, atk, pwr, pr, mr, exp =None, loot =None, skills =None):
    def __init__(self, name, stats =None, loot =None, skills =None):
        if not stats:
            stats = enemy_base_stats[name]
        if not loot:
            loot = enemy_items[name]
        if not skills:
            skills = enemy_skills[name]

        Fighter.__init__(self, name, stats, loot, skills)
    '''
        self.name = name
        self.hp = stats['HP']
        self.atk = stats['ATK']
        self.pwr = stats['PWR']
        self.res = stats['RES']
        self.mr = stats['MR']
        self.exp = stats['EXP']
        self.stats = stats
        self.loot = loot
        self.skills = skills
    '''

    def fight_turn(self, foe):
        self.attack(foe)
        print foe.hp

    def reward(self):
        if self.loot:
            return choice(self.loot)    # Item object
        return None

'''  FIGHTER method
    def attack(self, foe):
        foe.hp -= self.atk
        print "%s deals %i dmg !" % (self.name, self.atk)


# Enemy : Soul
# bad because same enemy instance every fight (stats, etc...)
zelda_soul = Enemy('Soul')
boktai_soul = Enemy('Soul')
castle_soul = Enemy('Soul')
'''