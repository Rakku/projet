#!/bin/python
from console_ui import print_fight_choices, print_enemy_killed

from fighter import *
#from items.items import item_classes
#from skills import Tourment
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

    # NEED OBJECTS for stuff
        self.stuff = []
        self.equipped = {
            "Head": None,
            "Body": None,
            "Legs": None,
            "Weapon": None
        }
        self.pos = [0, 0]

    ### GENERICS

    ### STAT FUNCS
    def check_stats(self):
        for stat, value in self.stats.iteritems():
            self.stats[stat] = max(value, 0)
            self.stats[stat] = min(value, self.max_stats[stat])

    ### ITEM FUNCS
    def know_item(self, item_name):
        return item_name in self.items

    def has_item(self, item_name):
        # name = name.class_name()
        return self.know_item(item_name) and self.items[item_name] > 0

    def add_item(self, item_name, qtity=1):
        if my_import('items.items', item_name):
            if self.has_item(item_name):
                self.items[item_name] += qtity
            else:
                self.items[item_name] = qtity
                print "new item !"

    # Case              =>      return, qtity, stats

    # has not item      =>      False, same, same
    # has item
    #   FullStats       =>      False, same, same
    #   ZeroStats       =>      False, same, same
    #   Stats OK        =>      True, -= 1, += bonus_stats

    # Maybe divide : call consume / use / equip selon item_type
    def use_item(self, item_name):
        used = False
        if self.has_item(item_name):
            # if item.requirement(self):
            #   item.use()
            item = my_import('items.items', item_name)
            if self.full_stats(item().bonus_stats):
                print "Can't use that : Full stats"
            elif self.zero_stats(item().bonus_stats):
                print "Can't use that : Zero stats"
            else:
                item().use(self.stats)
                self.items[item_name] -= 1
                self.check_stats()
                print "%s used !" % item_name
                used = True
        else:
            print "Don't have any of that (%s)" % item_name
        return used

    ### SKILL FUNCS #
    def know_skill(self, skill_name):
        return skill_name in self.skills.keys()

    def learn_skill(self, skill_name):
        skill = load_hero_skill(skill_name)
        if skill:
            if not self.know_skill(skill_name):
                self.skills[skill_name] = 1
                print "%s a appris un sort : %s %i" % (self.name, skill_name, self.skills[skill_name])
                return True
            else:
                print "%s connait deja %s %i" % (self.name, skill_name, self.skills[skill_name])
        return False

    def cast_skill(self, skill_name):
        if self.know_skill(skill_name):
            skill = my_import('skills', skill_name)
            stats = self.stats
            new_stats = skill().cast(stats)

            if new_stats != stats:
                print "Skill reached target !"
            else:
                print "Skill missed !"
            return True
        return False

    ### FIGHT FUNCS #TODO : tests
    # def attack(self, enemy):
    #     enemy.stats['HP'] -= self.stats['ATK']

    def kill(self, enemy):
        print enemy.items
        gain = enemy.reward()
        print gain
        self.stats['EXP'] += enemy.stats['EXP']
        if gain:
            self.add_item(gain)
        print_enemy_killed(enemy, gain)

    def fight_turn(self, enemy):
        print_fight_choices()
        # wait
        raw_input()
        self.attack(enemy)
