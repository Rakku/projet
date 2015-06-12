#!/bin/python

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
    def __init__(self, name, spec, items ={}, skills ={}):
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
            Potion : 2
        }
        #self.equipped = []
        # List of Skill objects
        self.skills = skills

        self.pos = [0, 0]

    ### GENERICS
    # list = { Object : 'name' }
    def search(self, name, list):
        for obj in list.keys():
            if obj.name == name:
                return obj
        return None

    ### STAT FUNCS
    def missing_hp(self):
        return self.stats['HP'] - self.hp

    ### ITEM FUNCS
    def search_item(self, item_name):
        return self.search(item_name, self.items)


    def add_item(self, item, qtity =1):
        #item = self.search(item_name, item_table)
        if item is not None:
            #print item.name
            if item in self.items.keys() and self.items[item] > 0:
                self.items[item] += qtity
            else:
                self.items[item] = qtity

    def use_item(self, item_name):
        item = self.search_item(item_name)
        if item is not None:
            if self.items[item] > 0:
                if item.use(self):
                    self.items[item] -= 1
                else:
                    print "can't use %s !" % item.name
            else:
                print "Don't have any of that (%s)" % item_name
        else:
            print "Wat is dat ?!"

    ### SKILL FUNCS
    def search_skill(self, skill_name):
        return self.search(skill_name, self.skills)

    def learn_skill(self, skill_name):
        skill = self.search(skill_name, skill_table)
        if skill is not None:
            self.skills[skill] = 1
            print "%s a appris un sort : %s %i" % (self.name, skill.name, self.skills[skill])

    def cast_skill(self, skill_name):
        skill = self.search_skill(skill_name)
        if skill is not None:
            if skill.cast():      # Func use_fireball, use_iceball, ...
                print "Skill reached target !"
            else :
                print "Skill missed !"

    ### FIGHT FUNCS
    def attack(self, enemy):
        enemy.hp -= self.atk

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

