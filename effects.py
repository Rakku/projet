#!/bin/python

# TODO : complete progressively


def gain_stat(stat, value, max_stat):
    if stat == 0:
        return 0
    new_stat = stat + value
    return min(stat + value, max_stat)

def gain_multi_stats(stats, values, max_stats):
    res =[]
    pass

def loose_stat(stat, value):
    return max(stat - value, 0)


def gain_hp(target, value=0):
    if target is not None:
        if target.is_full_hp():
            print "No need to use this : FULL HP"
            return False
        if target.hp == 0:
            print "Can't use this on dead people"
            return False
        if target.missing_hp() < value:
            value = target.missing_hp()
            # target.hp = target.stats['HP']
        # else:
        target.hp += value
        print "+ %i HP" % value
        target.print_hp()
        return True
    return False


def deal_dmg(target, value=1):
    if target is not None:
        # target = Glob.hero OR target = enemy() (INSTANCE)
        target.hp -= value
        print "- %i HP" % value
        target.print_hp()
        return True
    return False
