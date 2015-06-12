#!/bin/python

from items import *
from skills import *
from console_ui import *

class Fighter:
    #def __init__(self, name, hp, atk, pwr, pr, mr, exp =None, loot =None, skills =None):
    def __init__(self, name, stats =None, items =None, skills =None):
        self.name = name
        if stats:
            self.hp = stats['HP']
            self.atk = stats['ATK']
            self.pwr = stats['PWR']
            self.res = stats['RES']
            self.mr = stats['MR']
            self.exp = stats['EXP']
            self.stats = stats
        if items:
            self.items = items
        if skills:
            self.skills = skills

    def attack(self, foe):
        foe.hp -= self.atk
        print "%s deals %i dmg !" % (self.name, self.atk)

    def missing_hp(self):
        return self.stats['HP'] - self.hp