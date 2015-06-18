from unittest import TestCase
from enemies import *

__author__ = 'p076085'


class TestEnemy(TestCase):
    def setUp(self):
        self.soul = Soul()
        self.specter = Specter()

    def test_enemy_init(self):
        self.assertDictEqual(self.soul.stats, Soul.stats)
        self.assertDictEqual(self.soul.items, Soul.items)
        self.assertDictEqual(self.soul.skills, Soul.skills)
        self.assertDictEqual(self.specter.stats, Specter.stats)
        self.assertDictEqual(self.specter.items, Specter.items)
        self.assertDictEqual(self.specter.skills, Specter.skills)

