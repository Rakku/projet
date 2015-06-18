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


#######################
###   ITEM CLASSES  ###
#######################


class Potion(Item):
    default = 5
    stat = 'HP'

    def __init__(self, value=default):
        self.value = value
        Item.__init__(self)

    # add value to stat with total < max_stat
    def use(self, stat, max_stat):
        new_hp = effects.gain_stat(stat, self.value, max_stat)
        # TODO : return stats ?
        return new_hp

class Elixir(Potion):
    def __init__(self):
        Potion.__init__(self, 50)


class Stone(Item):
    default = 1

    def __init__(self, stat='', value=default):
        self.value = value
        if stat == '':
            stat = 'HP'
        self.stat = stat
        Item.__init__(self)

    # add value to stat
    def use(self, stat):
        return stat + self.value


# Equipment
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

    def equip(self, stats):
        res = {}
        if self.equipped:
            # Unequip
            for stat in stats:
                #res[stat] = stats[stat] - self.bonus_stats[stat]
                stats[stat] -= self.bonus_stats[stat]
            self.equipped = False
        else:
            # Equip
            for stat in stats:
                #res[stat] = stats[stat] + self.bonus_stats[stat]
                stats[stat] += self.bonus_stats[stat]
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
