#!/bin/python

# TODO : LATER

# need instance of Enemy
def fight(hero, enemy):
    while enemy.stats['HP'] > 0 and hero.stats['HP'] > 0:
        enemy.fight_turn(hero)
        hero.fight_turn(enemy)
        print "Hero HP : %i / %i" % (hero.stats['HP'], hero.max_stats['HP'])

    if hero.stats['HP'] > 0:
        hero.kill(enemy)

