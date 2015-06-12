#!/bin/python

# need instance of Enemy
def fight(hero, enemy):
    while enemy.hp > 0 and hero.hp > 0:
        enemy.fight_turn(hero)
        hero.fight_turn(enemy)

    if hero.hp > 0:
        hero.kill(enemy)

