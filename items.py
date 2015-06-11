#!/bin/python

import effects


#######################
###   CLASSES       ###
#######################
'''
class Item:
    def __init__(self, name, cost =50, text =''):
        self.name = name
        #self.effect = effect        # Pre defined function
        self.cost = cost
        self.text = text

    #def use(self):
'''


#######################
###   ITEM CLASSES  ###
#######################

class Potion:
    name = 'potion'
    text = '+5 HP'

    @staticmethod
    def use(target, t =text):
        if effects.gain_hp(target, hp=5):
            print t
            return True
        return False

class Sirop:
    name = 'sirop'
    text = '+3 HP'

    @staticmethod
    def use(target, t =text):
        if effects.gain_hp(target, hp=3):
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
###  ITEM=>NAME TABLES  ###
###########################

item_table = {
    Potion: 'potion',
    Sirop: 'sirop'
    #'amulette': 2,
    #'croc': 1,
    #'poil': 1
}


'''
class Item:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type
        self.effect = effect

potion = Item('potion', 'common', ['hp', '+', '20'])
sirop = Item('sirop', 'common', ['mp', '+', '40'])
amulette = Item('amulette', 'common', ['mr', '+', '10'])
croc = Item('croc', 'common', ['atk', '+', '5'])
poil = Item('poil', 'frequent', [])
'''