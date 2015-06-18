import random

from unittest import TestCase
from items.items import *

__author__ = 'Kazesoushi'


class TestItem(TestCase):
    def setUp(self):
        # base stats before item use/equip/whatever
        self.stats = {
            'HP': 20,
            'ATK': 0,
            'PWR': 0,
            'RES': 10,
            'MR': 5,
            'EXP': 0
        }
        self.max_stats = {
            'HP': 50,
            'ATK': 0,
            'PWR': 0,
            'RES': 30,
            'MR': 5,
            'EXP': 0
        }
        self.item = Potion()
        self.stat = random.randint(0, 8)
        self.max_stat = random.randint(8, 15)

    '''
    # @mock.patch('items.items.effects')
    def test_item_use(self):
        for item in item_classes:
            print "TEST %s.use()" % item.class_name()
            print item.text
            new_stat = item.use(self.stat, self.max_stat)
            diff_stat = new_stat - self.stat
            print "%s.use(%i,%i) return %i" % (item.class_name(), self.stat, self.max_stat, new_stat)

            # Verif conformite stats
            self.assertTrue(new_stat == min(self.stat + item.value, self.max_stat) or new_stat == 0)
            self.assertTrue(diff_stat == item.value or new_stat == self.max_stat or new_stat == 0, msg="+ %i stat(%i), "
                                                                                       "stat = %i->%i/%i" % (
                diff_stat, item.value, self.stat, new_stat, self.max_stat))
    '''

    # POTIONS
    def test_potion_use_zero(self):
        #value = random.randint(0, 100)
        item = Potion({'HP': 0})
        old = self.stats
        max = random.randint(0, 100)
        item.use(self.stats, self.max_stats)
        self.assertEqual(old, self.stats)

    def test_potion_use_value(self):
        #item = Potion(value)
        # TODO : Typically is it better to test Potion(random) or Elixir() & Sirop() & ... ?
        #item = Elixir()
        #value = item.value
        old = self.stats.copy()
 #       stat = random.randint(1, 100)
#        max = random.randint(0, 100) + stat + item.value # max > stat + value
        self.item.use(self.stats, self.max_stats)
        #print self.stats
        #print old
        for stat in self.item.bonus_stats:
            self.assertEqual(self.stats[stat], old[stat] + self.item.bonus_stats[stat])

    '''
    def test_potion_use_max(self):
        value = random.randint(0, 100)
        #item = Potion(value)
        stat = random.randint(1, 100)
        max = random.randint(0, stat + value) # max <= stat + value
        old = self.stats
        self.item.use(self.stats, self.max_stats)
        for stat in self.item.bonus_stats:
            self.assertEqual(self.stats[stat], old[stat] + self.item.bonus_stats[stat])
    '''

    # STONES
    def test_stone_use(self):
        value = random.randint(0, 100)
        item = Stone(value=value)
        stat = random.randint(0, 100)
        self.assertEqual(item.use(stat), stat + value)

    # STUFF
    def test_stuff_equip(self):
        item = Stuff()
        # equip
        old = self.stats.copy()
        item.equip(self.stats)
        for stat in self.stats:
            self.assertEqual(old[stat] + item.bonus_stats[stat], self.stats[stat])
        self.assertTrue(item.equipped)
        # unequip
        old = self.stats.copy()
        item.equip(self.stats)
        for stat in self.stats:
            self.assertEqual(old[stat] - item.bonus_stats[stat], self.stats[stat])
        self.assertFalse(item.equipped)

