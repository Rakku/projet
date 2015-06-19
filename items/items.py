#!/bin/python

import sys
import inspect

import effects
from named import Named


#######################
###   CLASSES       ###
#######################

class Item(Named):
    def __init__(self, cost=50, text=''):

        # self.effect = effect        # Pre defined function
        self.cost = cost
        if text == '':
            text = "+ %i %s" % (self.value, self.stat)
        self.text = text


class ItemAlt(Named):
    def __init__(self, cost=50, text=''):
        self.cost = cost
        if text == '':
            for stat in self.bonus_stats:
                if self.bonus_stats[stat] != 0:
                    text = "+ %i %s\n" % (self.bonus_stats[stat], stat)
        self.text = text

    def requirement(self, hero):
        raise NotImplementedError

#######################
###   ITEM CLASSES  ###
#######################

#
# POTIONS : TEMP STATS MODIFS
#
class Potion(ItemAlt):
    # default = 5
    # stat = 'HP'
    stats = {'HP': 5}

    def __init__(self, bonus=stats):
        self.bonus_stats = bonus
        ItemAlt.__init__(self)

    # TO NOT TEST
    def requirement(self, hero):
        if hero.full_stats(self.bonus_stats) or hero.zero_stats(self.bonus_stats):
            return False
        return True

    def use(self, stats):
        for stat in self.bonus_stats:
            if stats[stat] > 0:
                stats[stat] += self.bonus_stats[stat]
        # effects.gain_stats(stats, self.bonus_stats, max_stats)


class Elixir(Potion):
    def __init__(self):
        Potion.__init__(self, {'HP': 50})


#
# STONES : PERMA MAX STATS MODIFS
#
class Stone(ItemAlt):
    stats = {'HP': 3}

    def __init__(self, bonus=stats):
        self.bonus_stats = bonus
        ItemAlt.__init__(self)

    def requirement(self, hero):


    # add value to stat
    def use(self, max_stats):
        for stat in self.bonus_stats:
            max_stats[stat] += self.bonus_stats[stat]


#
# STUFF : MAX STATS MODIFS WHILE EQUIPPED
#
class Stuff(ItemAlt):
    bonus_stats = {
        'HP': 0,
        'ATK': 0,
        'PWR': 0,
        'RES': 10,
        'MR': 5,
        'EXP': 0
    }

    def __init__(self, stats=bonus_stats):
        self.bonus_stats = stats
        self.equipped = False
        ItemAlt.__init__(self)

    def equip(self, max_stats):
        if self.equipped:
            # Unequip
            for stat in max_stats:
                #res[stat] = stats[stat] - self.bonus_stats[stat]
                max_stats[stat] -= self.bonus_stats[stat]
            self.equipped = False
        else:
            # Equip
            for stat in max_stats:
                #res[stat] = stats[stat] + self.bonus_stats[stat]
                max_stats[stat] += self.bonus_stats[stat]
            self.equipped = True
        #return res


'''


)
class Sirop:
    text = '+3 HP'

    @staticmethod
    def use(target, t =text):
        print t
        effects.gain_hp(target, hp=3)

class Sirop:
    text = '+3 HP'

    @staticmethod
    def use(target, t =text):
        print t
        effects.gain_hp(target, hp=3)

class Sirop:
    text = '+3 HP'

    @staticmethod
    def use(target, t =text):
        print t
        effects.gain_hp(target, hp=3)

#class Amulette:

'''

###########################
###  NAME=>ITEM TABLES  ###
###########################

def fill_item_classes():
    list = []
    usables = []
    equips = []
    # name = Soul, obj = enemies.Soul
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        print name, obj
        if obj.__module__ == __name__ and name != 'Item':
            list.append(obj())
            if callable(getattr(obj, "use", None)):
                usables.append(obj())
            elif callable(getattr(obj, "equip", None)):
                equips.append(obj())
    return list, usables, equips


#item_classes, usables, equips = fill_item_classes()

#
# item_table = {
#     'potion': Potion,
#     'sirop': Sirop,
#     # 'amulette': 2,
#     # 'croc': 1,
#     # 'poil': 1
# }
