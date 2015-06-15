from unittest import TestCase
import random
from hero import *

__author__ = 'Kazesoushi'


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero()

    def test_hero_init(self):
        print "TEST HERO CREATION"
        print "Name : %s" % self.hero.name
        # print "Spec OK"
        self.assertEquals(self.hero.level, 1)
        print "Level OK"
        self.assertDictEqual(hero_base_stats[self.hero.spec], self.hero.stats)
        print "Stats Dict OK"
        self.assertDictEqual(base_items[self.hero.spec], self.hero.items)
        print "Items Dict OK"
        self.assertDictEqual(base_skills[self.hero.spec], self.hero.skills)
        print "Skills Dict OK"

    # TODO : separate ?
    def test_know_has_item(self):
        for item_name in self.hero.items:
            self.assertTrue(self.hero.know_item(item_name))
            print "%s knows item %s" % (self.hero.name, item_name)
            self.assertEqual(self.hero.has_item(item_name), self.hero.items[item_name] > 0)
            print "%s has item %s" % (self.hero.name, item_name)

    def test_know_item_yes(self):
        self.hero.items["Potion"] = 0
        self.assertTrue(self.hero.know_item("Potion"))
        self.hero.items["Sirop"] = 5
        self.assertTrue(self.hero.know_item("Sirop"))

    def test_know_item_no(self):
        self.hero.items["Sirop"] = 2
        self.hero.items.pop("Sirop")
        self.assertFalse(self.hero.know_item("Sirop"))

    def test_has_item_yes(self):
        self.hero.items["Potion"] = random.randint(1, 12)
        self.assertTrue(self.hero.has_item("Potion"))

    def test_has_item_no(self):
        self.hero.items["Potion"] = 0
        self.assertFalse(self.hero.has_item("Potion"))
        self.hero.items.pop("Potion")
        self.assertFalse(self.hero.has_item("Potion"))

    # TODO : more simple ?
    def test_add_item(self):
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

    '''
    # TESTED in add_item_qtity_default
    def test_add_item_existing(self):
        self.hero.add_item("Potion")
        self.assertTrue(self.hero.items["Potion"] > 0)
    '''

    # Most Excluding Case First
    def test_add_item_notexisting(self):
        self.hero.add_item("Hibou")
        self.assertFalse("Hibou" in self.hero.items.keys())

    def test_add_item_notknown(self):
        self.hero.add_item("ResBoost")
        self.assertTrue("ResBoost" in self.hero.items.keys())

    def test_add_item_qtity_default(self):
        qtity = self.hero.items["Potion"]
        self.hero.add_item("Potion")
        self.assertEqual(qtity + 1, self.hero.items["Potion"])

    def test_add_item_qtity_ok(self):
        n = random.randint(0,5)
        qtity = self.hero.items["Potion"]
        self.hero.add_item("Potion", n)
        self.assertEqual(qtity + n, self.hero.items["Potion"])

    def test_use_item(self):
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
        self.hero.use_item("Potion")
        self.assertEqual(3, self.hero.items["Potion"])

    # Skill test suite : Most Exclusive Case first
    def test_know_skill(self):
        for skill_name in self.hero.skills:
            print "TEST Hero.know_skill(%s)" % skill_name
            self.assertTrue(self.hero.know_skill(skill_name))
            print "%s knows %s" % (self.hero.name, skill_name)

    def test_learn_skill(self):
        print "TEST Hero.learn_skill(Cri)"
        self.hero.learn_skill('Cri')
        self.assertTrue(self.hero.know_skill('Cri'))

    def test_cast_skill(self):
        pass