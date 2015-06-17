from unittest import TestCase
from skills import *

__author__ = 'Kazesoushi'


class TestSkill(TestCase):
    def setUp(self):
        # base stats before skill effect is applied
        self.stats = {
            'HP': 30,
            'ATK': 0,
            'PWR': 0,
            'RES': 10,
            'MR': 5,
            'EXP': 0
        }
        self.skill = Skill()

    def test_skill_init(self):
        for stat in self.skill.stat_effects.keys():
            self.assertTrue(stat in self.stats.keys())

    def test_skill_cast(self):
        old = self.stats.copy()
        self.skill.cast(self.stats)
        for stat in self.skill.stat_effects:
            self.assertEqual(self.stats[stat], old[stat] + self.skill.stat_effects[stat])