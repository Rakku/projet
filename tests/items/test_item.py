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
        self.item = Potion()

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
    def test_potions_init(self):
        item = Elixir()
        self.assertEqual(item.bonus_stats, {'HP': 50})

    def test_potion_use(self):
        item = Potion()
        old = self.stats.copy()
        item.use(self.stats)
        for stat, value in item.bonus_stats.iteritems():
            self.assertEqual(self.stats[stat], old[stat] + value)

    # STONES
    def test_stone_use(self):
        item = Stone()
        old = self.stats.copy()
        item.use(self.stats)
        for stat, value in item.bonus_stats.iteritems():
            self.assertEqual(self.stats[stat], old[stat] + value)

    # STUFF
    def test_stuff_equip(self):
        item = Stuff()
        # equip
        uneq = self.stats.copy()
        item.equip(self.stats)
        for stat, value in item.bonus_stats.iteritems():
            self.assertEqual(self.stats[stat], uneq[stat] + value)
        self.assertTrue(item.equipped)
        # unequip
        eq = self.stats.copy()
        item.equip(self.stats)
        for stat, value in item.bonus_stats.iteritems():
            self.assertEqual(self.stats[stat], eq[stat] - value)
        self.assertFalse(item.equipped)

