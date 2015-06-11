#!/bin/python

from console_ui import *
from items import *
from skills import *
from fighter import *

hero_base_stats = {
    'Warrior': {
        'HP': 25,
        'ATK': 10,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 0
    },
    'Mage': {
        'HP': 18,
        'ATK': 4,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 0
    },
    'Assassin': {
        'HP': 12,
        'ATK': 20,
        'PWR': 0,
        'RES': 0,
        'MR': 5,
        'EXP': 0
    }
}

class Hero(Fighter):
    def __init__(self, name, spec, items = { }, skills =[]):
        Fighter.__init__(self, name, hero_base_stats[spec], items, skills)

        self.spec = spec

        '''
        self.stats = hero_base_stats[spec]
        self.hp = self.stats['HP']
        self.atk = self.stats['ATK']
        self.pwr = self.stats['PWR']
        self.res = self.stats['RES']
        self.mr = self.stats['MR']
        self.exp = self.stats['EXP']
        '''
        self.level = 1

        # dict (item_name : qtity)
        self.items = {
            'potion' : 2
        }
        # List of Skill objects
        #self.skills = skills

        self.pos = [0, 0]

    def missing_hp(self):
        return self.stats['HP'] - self.hp

    def learn_skill(self, skill_name):
        if skill_name in skill_func.keys():
            self.skills.append(skill_name)
            print self.name + " a appris un sort : " + skill_name

    def cast_skill(self, skill_name):
        if skill_name in self.skills:
            skill_func[skill_name]      # Func use_fireball, use_iceball, ...


    def attack(self, enemy):
        enemy.hp -= self.atk

    def add_item(self, item_name, qtity =1):
        if item_name in self.items.keys():
            self.items[item_name] += qtity
        else:
            self.items[item_name] = qtity

    def use_item(self, item_name):
        if item_name in self.items.keys():
            if self.items[item_name] > 0:
                if use_item_func[item_name](self):     # Func use_potion, use_sirop, ...
                    self.items[item_name] -= 1
                else:
                    print "Can't use %s" % item_name
            else:
                print "Don't have any %s" %item_name
        else:
            print "Don't know what that actually is"

    def kill(self, enemy):
        gain = enemy.reward()
        self.exp += enemy.exp
        self.add_item(gain)
        print_enemy_killed(enemy, gain)



    def fight_turn(self, enemy):
        print_fight_choices()
        # wait
        raw_input()
        self.attack(enemy)

