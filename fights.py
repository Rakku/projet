#!/bin/python

# TODO : LATER
# TODO : RE-ADAPT TO stats[] / max_stats[] FORMAT (currently hp / stat['HP'])

# need instance of Enemy
def fight(hero, enemy):
    while enemy.stats['HP'] > 0 and hero.stats['HP'] > 0:
        enemy.fight_turn(hero)
        hero.fight_turn(enemy)

    if hero.stats['HP'] > 0:
        hero.kill(enemy)

