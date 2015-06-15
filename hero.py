#!/bin/python
from console_ui import print_fight_choices, print_enemy_killed

from fighter import *
from items.items import item_classes
from skills import Tourment
from load import my_import


# TODO : fight Funcs (LATER)

def load_hero_skill(skill_name):
    return my_import('skills', skill_name)

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

base_items = {
    'Warrior': {"Potion": 2},
    'Mage': {"Potion": 1},
    'Assassin': {"Potion": 1}
}

base_skills = {
    'Warrior': {},
    'Mage': {"Tourment": 1},
    'Assassin': {"Tourment": 1}
}


class Hero(Fighter):
    def __init__(self, name='Heroik', spec='Mage', items=None, skills=None):
        Fighter.__init__(self, hero_base_stats[spec], base_items[spec], base_skills[spec])

        self.name = name
        self.spec = spec
        self.level = 1

        self.pos = [0, 0]

    ### GENERICS

    ### STAT FUNCS


    ### ITEM FUNCS
    def know_item(self, item_name):
        return item_name in self.items

    def has_item(self, name):
        # name = name.class_name()
        return self.know_item(name) and self.items[name] > 0

    def add_item(self, item_name, qtity=1):
        if my_import('items.items', item_name):
            if self.has_item(item_name):
                self.items[item_name] += qtity
            else:
                self.items[item_name] = qtity

    def use_item(self, item_name):
        item = my_import('items.items', item_name)
        if item and self.has_item(item_name):
            if not self.full_stat(item.stat):
                self.stats[item.stat] = item.use(self.stats[item.stat], self.max_stats[item.stat])
                self.items[item_name] -= 1
                print "%s used !" % item_name
                return True
            else:
                print "Can't use that : %s full" % item.stat
        else:
            print "Don't have any of that (%s)" % item_name
        return False

    ### SKILL FUNCS #
    def know_skill(self, skill_name):
        return skill_name in self.skills.keys()


    def learn_skill(self, skill_name):
        skill = load_hero_skill(skill_name)
        if skill:
            if not self.know_skill(skill_name):
                self.skills[skill_name] = 1
                print "%s a appris un sort : %s %i" % (self.name, skill_name, self.skills[skill_name])
            else:
                print "%s connait deja %s %i" % (self.name, skill_name, self.skills[skill_name])

    def cast_skill(self, skill_name):
        if self.know_skill(skill_name):
            skill = my_import('skills', skill_name)
            stat = self.stats[skill.stat]
            new_stat = skill.cast(stat)

            if new_stat != stat:
                print "Skill reached target !"
            else:
                print "Skill missed !"

    ### FIGHT FUNCS #TODO : tests
    # def attack(self, enemy):
    #     enemy.stats['HP'] -= self.stats['ATK']

    def kill(self, enemy):
        gain = enemy.reward()
        self.exp += enemy.exp
        self.add_item(gain.class_name())
        print_enemy_killed(enemy, gain)

    def fight_turn(self, enemy):
        print_fight_choices()
        # wait
        raw_input()
        self.attack(enemy)
