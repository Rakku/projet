import random

from unittest import TestCase
from items.items import *

__author__ = 'Kazesoushi'


class TestItem(TestCase):
    def setUp(self):
        self.items = item_classes
        self.stat = random.randint(0, 8)
        self.max_stat = random.randint(8, 15)

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

    def test_item_use_value(self):
        for item in item_classes:
            diff = item.use(100, 1500) - 100
            if diff < 0:
                diff = -diff
            self.assertEqual(diff, item.value)

    def test_item_use_max(self):
        for item in item_classes:
            self.assertEqual(item.use(1,2), 2)