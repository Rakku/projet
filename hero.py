#!/bin/python
from console_ui import print_fight_choices, print_enemy_killed

from fighter import *
from items.items import Potion, item_table
from skills import Tourment, skill_table

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

hero_base_items = {
    'Warrior': {Potion: 2},
    'Mage': {Potion: 1},
    'Assassin': {Potion: 1}
}

hero_base_skills = {
    'Warrior': {},
    'Mage': {Tourment: 1},
    'Assassin': {Tourment: 1}
}


class Hero(Fighter):
    def __init__(self, name, spec, items=None, skills=None):
        Fighter.__init__(self, name, hero_base_stats[spec], hero_base_items[spec], hero_base_skills[spec])

        self.spec = spec
        self.level = 1

        # dict (Item : qtity)
        self.items = {
            Potion: 2
        }
        # dict (Skill : level)
        self.skills = skills

        self.pos = [0, 0]

        if items is None:
            items = {}
        self.items = items

        if skills is None:
            skills = {}
        self.skills = skills

    ### GENERICS
    # dico = { 'name': Object }
    def search(self, name, dico):
        for obj in dico.keys():
            if obj.name == name:
                return obj
        return None

    ### STAT FUNCS
    '''
    DEFINED in fighter.py
    def missing_hp(self):

    '''

    ### ITEM FUNCS
    def search_item(self, item_name):
        return self.search(item_name, self.items)

    def add_item(self, item_name, qtity=1):
        item = self.search(item_name, item_table)
        if item is not None:
            # print item.name
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
        if skill:  # is not None:
            known = self.search(skill_name, self.skills)
            if not known:
                self.skills[skill] = 1
                print "%s a appris un sort : %s %i" % (self.name, skill.name, self.skills[skill])
            else:
                print "%s connait deja %s %i" % (self.name, skill.name, self.skills[skill])

    def cast_skill(self, skill_name):
        skill = self.search_skill(skill_name)
        if skill is not None:
            if skill.cast():  # Func use_fireball, use_iceball, ...
                print "Skill reached target !"
            else:
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
