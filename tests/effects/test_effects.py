from unittest import TestCase

import random
import effects

__author__ = 'Kazesoushi'


class TestEffects(TestCase):
    def setUp(self):
        self.stat = random.randint(0, 8)
        self.max_stat = random.randint(8, 15)
        self.value = random.randint(0,7)

    def test_gain_stat(self):
        print "TEST GAIN_STAT"
        new_stat = effects.gain_stat(self.stat, self.value, self.max_stat)
        diff_stat = new_stat - self.stat
        print "gain_stat(%i,%i,%i) return %i" % (self.stat, self.value, self.max_stat, new_stat)

        self.assertTrue(new_stat <= self.max_stat, msg="Max stat overflow")
        # Cases:
        # Stat = 0                   return 0
        # Stat + value > max_stat    return max_stat
        # else                       return Stat + value
        self.assertTrue(new_stat == 0 or new_stat == self.max_stat or diff_stat == self.value, msg="Wrong stat gain ")

    # Divided test_gain_stat :
    def test_gain_stat_value(self):
        self.assertEqual(effects.gain_stat(2, 5, 8), 7)

    def test_gain_stat_max(self):
        self.assertEqual(effects.gain_stat(6, 5, 9), 9)

    def test_gain_stat_zero(self):
        self.assertEqual(effects.gain_stat(0, 6, 9), 0)

    def test_loose_stat(self):
        print "TEST LOOSE_STAT"
        new_stat = effects.loose_stat(self.stat, self.value)
        diff_stat = self.stat - new_stat
        print "loose_stat(%i,%i) return %i" % (self.stat, self.value, new_stat)

        self.assertTrue(self.max_stat >= new_stat >= 0, msg="Min stat underflow")
        self.assertTrue(diff_stat == self.value or new_stat == 0, msg="Wrong stat loss")

    # Divided test_loose_stat:
    def test_loose_stat_value(self):
        self.assertEqual(effects.loose_stat(8, 5), 3)

    def test_loose_stat_value(self):
        self.assertEqual(effects.loose_stat(4, 6), 0)