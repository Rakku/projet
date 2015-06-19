from unittest import TestCase
import random
from hero import *

__author__ = 'Kazesoushi'


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero()

    def test_hero_init(self):
        print "TEST HERO CREATION"
        print "Name : %s, %s" % (self.hero.name, self.hero.spec)
        self.assertEquals(self.hero.level, 1)
        print "Level OK"
        self.assertDictEqual(hero_base_stats[self.hero.spec], self.hero.stats)
        print "Stats Dict OK"
        self.assertDictEqual(base_items[self.hero.spec], self.hero.items)
        print "Items Dict OK"
        self.assertDictEqual(base_skills[self.hero.spec], self.hero.skills)
        print "Skills Dict OK"

    # TODO : Useless ?
    # Typically : Inter-dependent double check :
    # 1/ hero.items tested with know_item, has_item (=> test_init_items) DONE above
    # 2/ know_item, has_item tested by admitting hero.items is OK (=> test_know_has_item) DONE below
    def test_know_has_item(self):
        for item_name in self.hero.items:
            self.assertTrue(self.hero.know_item(item_name))
            print "%s knows item %s" % (self.hero.name, item_name)
            self.assertEqual(self.hero.has_item(item_name), self.hero.items[item_name] > 0)
            print "%s has item %s" % (self.hero.name, item_name)

    def test_know_item(self):
        # Knows
        self.hero.items["Potion"] = 0
        self.assertTrue(self.hero.know_item("Potion"))
        # Has (include Knows aka above useless)
        self.hero.items["Sirop"] = 5
        self.assertTrue(self.hero.know_item("Sirop"))
        # not Knows
        self.hero.items.pop("Sirop")
        self.assertFalse(self.hero.know_item("Sirop"))
        # not existing
        self.assertFalse(self.hero.know_item("Hibou"))

    def test_has_item(self):
        # Has
        self.hero.items["Potion"] = 2   # random.randint(1, 12)
        self.assertTrue(self.hero.has_item("Potion"))
        # Knows
        self.hero.items["Potion"] = 0
        self.assertFalse(self.hero.has_item("Potion"))
        # not Knows
        self.hero.items.pop("Potion")
        self.assertFalse(self.hero.has_item("Potion"))

    def test_add_item(self):
        self.hero.items["Potion"] = 0
        # Default qtity = 1
        self.hero.add_item("Potion")
        self.assertEqual(self.hero.items["Potion"], 1)
        # Set qtity
        self.hero.add_item("Potion", 4)
        self.assertEqual(self.hero.items["Potion"], 5)
        # Item not existing
        self.hero.add_item("Hibou", 4)
        self.assertFalse("Hibou" in self.hero.items.keys())

    def test_use_item(self):

        self.hero.items["Potion"] = 2
        # Use : False / has item, HP full (hero init test OK)
        print self.hero.stats
        print self.hero.max_stats
        self.assertFalse(self.hero.use_item("Potion"))
        self.assertEqual(self.hero.items["Potion"], 2)
        # self.assertEqual(self.hero.stats['HP'], self.hero.max_stats['HP'])    # checked in items
        # Use : True / has item, HP not full
        self.hero.stats['HP'] = 5
        self.assertTrue(self.hero.use_item("Potion"))
        self.assertEqual(self.hero.items["Potion"], 1)
        # self.assertEqual(self.hero.stats['HP'], 10)     # checked in items
        # Use : True / has item, HP empty (not supposed to occur)
        self.hero.stats['HP'] = 0
        self.assertFalse(self.hero.use_item("Potion"))
        self.assertEqual(self.hero.items["Potion"], 1)
        # self.assertEqual(self.hero.stats['HP'], 0)     # checked in items
        # Use : False / doesnt have item
        self.hero.items["Potion"] = 0
        self.assertFalse(self.hero.use_item("Potion"))
        self.assertEqual(self.hero.items["Potion"], 0)
        # self.assertEqual(self.hero.stats['HP'], 10)   # checked in items
        # Use : False / doesnt know item
        self.hero.items.pop("Potion")
        self.assertFalse(self.hero.use_item("Potion"))
        self.assertFalse("Potion" in self.hero.items)
        # self.assertEqual(self.hero.stats['HP'], 10)   # checked in items
        # Use : False / item doesnt exist
        self.assertFalse(self.hero.use_item("Hibou"))
        self.assertFalse("Hibou" in self.hero.items)
        # self.assertEqual(self.hero.stats['HP'], 10)   # checked in items


    # TODO : more simple ?
    def test_add_item_old(self):
        for item_name in self.hero.items:
            print "TEST Hero.add_item(%s)" % item_name
            n = random.randint(0, 5)
            qtity = self.hero.items[item_name]
            self.hero.add_item(item_name)
            self.assertTrue(self.hero.has_item(item_name))
            self.assertEqual(qtity + 1, self.hero.items[item_name])
            print "Default qtity = 1 OK"
            qtity = self.hero.items[item_name]
            self.hero.add_item(item_name, n)
            self.assertEqual(qtity + n, self.hero.items[item_name])
            print "Add n = %i OK" % n

    # Most Excluding Case First
    def test_add_item_notexisting(self):
        self.assertFalse(self.hero.add_item("Hibou"))
        self.assertFalse("Hibou" in self.hero.items.keys())

    '''
    def test_add_item_notknown(self):
        self.hero.add_item("ResBoost")
        self.assertTrue("ResBoost" in self.hero.items.keys())
    '''

    def test_add_item_qtity_default(self):
        qtity = self.hero.items["Potion"]
        self.hero.add_item("Potion")
        self.assertEqual(qtity + 1, self.hero.items["Potion"])

    def test_add_item_qtity_ok(self):
        n = random.randint(0,5)
        qtity = self.hero.items["Potion"]
        self.hero.add_item("Potion", n)
        self.assertEqual(qtity + n, self.hero.items["Potion"])

    def test_use_item_old(self):
        for item_name in self.hero.items:
            print "TEST Hero.use_item(%s)" % item_name
            qtity = self.hero.items[item_name]
            if self.hero.use_item(item_name):
                print "qtity : %i -> %i" % (qtity, self.hero.items[item_name])
                self.assertTrue(self.hero.items[item_name] == qtity - 1 or qtity == 0)

    def test_use_item_notowned(self):
        pass

    def test_use_item_owned(self):
        self.hero.items["Potion"] = 4
        # qtity = self.hero.items["Potion"]
        if self.hero.use_item("Potion"):
            self.assertEqual(3, self.hero.items["Potion"])

    # Skill test suite : Most Exclusive Case first
    def test_know_skill(self):
        # know
        self.hero.skills["Tourment"] = 1
        self.assertTrue(self.hero.know_skill("Tourment"))
        # Don't know
        self.hero.skills.pop("Tourment")
        self.assertFalse(self.hero.know_skill("Tourment"))
        '''
        for skill_name in self.hero.skills:
            print "TEST Hero.know_skill(%s)" % skill_name
            self.assertTrue(self.hero.know_skill(skill_name))
            print "%s knows %s" % (self.hero.name, skill_name)
        '''

    def test_learn_skill(self):
        self.hero.skills = {}
        # Existing skill
        self.assertTrue(self.hero.learn_skill('Cri'))
        self.assertTrue('Cri' in self.hero.skills)
        # Already known skill
        self.assertFalse(self.hero.learn_skill('Cri'))
        # Not existing skill
        self.assertFalse(self.hero.learn_skill('Potion'))
        self.assertFalse('Potion' in self.hero.skills)

    def test_cast_skill(self):
        # known skill
        self.assertTrue(self.hero.cast_skill('Tourment'))
        # unknown skill
        self.assertFalse(self.hero.cast_skill('Cri'))
        # not existing skill
        self.assertFalse(self.hero.cast_skill('Potion'))