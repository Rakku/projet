#!/bin/python

# TODO : LATER

from named import Named


class Fighter(Named):
    # def __init__(self, name, hp, atk, pwr, pr, mr, exp =None, loot =None, skills =None):
    def __init__(self, stats=None, items=None, skills=None):
        if stats:
            self.hp = stats['HP']
            self.atk = stats['ATK']
            self.pwr = stats['PWR']
            self.res = stats['RES']
            self.mr = stats['MR']
            self.exp = stats['EXP']
            self.stats = stats
            self.max_stats = stats

        # ITEMS : {
        if items is None:
            items = {}
        self.items = items

        if skills is None:
            skills = {}
        self.skills = skills

    def attack(self, foe):
        foe.hp -= self.atk
        print "%s deals %i dmg !" % (self.class_name(), self.atk)

    def print_hp(self):
        print "%s\nHP : %i / %i" % (self.class_name(), self.hp, self.stats['HP'])

    def full_stat(self, stat):
        return self.stats[stat] == self.max_stats[stat]

    def is_full_hp(self):
        return self.stats['HP'] == self.max_stats['HP']

    def missing_hp(self):
        return self.stats['HP'] - self.hp
