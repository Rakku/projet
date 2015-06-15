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

        #def use(self):


#######################
###   ITEM CLASSES  ###
#######################

class Potion(Item):
    value = 5
    stat = 'HP'


    @staticmethod
    def use(stat, max_stat):
        # return new_stat[stat]
        new_hp = effects.gain_stat(stat, Potion.value, max_stat)
        return new_hp

    @staticmethod
    def useitem(target=None, v=value, t=stat):
        #return hp + 5
        # print t
        # if target:
        #   target.gain_hp(value)
        if effects.gain_hp(target, value=v):
            return True
        return False


class Sirop(Item):
    value = 3
    stat = 'HP'

    @staticmethod
    def use(stat, max_stat):
        return effects.gain_stat(stat, Sirop.value, max_stat)

    @staticmethod
    def useitem(target=None, v=value, t=stat):
        if effects.gain_hp(target, value=v):
            print t
            return True
        return False


'''
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
    # name = Soul, obj = enemies.Soul
    for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        print name, obj
        if obj.__module__ == __name__ and name != 'Item':
            list.append(obj())
    return list


item_classes = fill_item_classes()

#
# item_table = {
#     'potion': Potion,
#     'sirop': Sirop,
#     # 'amulette': 2,
#     # 'croc': 1,
#     # 'poil': 1
# }
