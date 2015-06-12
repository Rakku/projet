#!/bin/python

def gain_hp(target, hp=0):
    hero = target
    if target.hp == target.stats['HP']:
        print "No need to use this : FULL HP"
        return False
    if target.missing_hp() < hp:
        target.hp = target.stats['HP']
    else:
        target.hp += hp
    print "%s\nHP : %i / %i" % (target.name, target.hp, target.stats['HP'])
    return True


def deal_dmg(target, dmg=1):
    if target is not None:
        target.hp -= dmg
        return True
    return False
