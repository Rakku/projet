#!/bin/python

# TODO : complete progressively

# TODO : change to void() func
def gain_stat(stat, value, max_stat):
    '''
    if stat != 0:
        stat = min(stat + value, max_stat)
    '''
    if stat == 0:
        return 0
    return min(stat + value, max_stat)

def gain_stats(stats, values, max_stats):
    for stat in values:
        stats[stat] = gain_stat(stats[stat], values[stat], max_stats[stat])
 #   return stats

def loose_stat(stat, value):
    # stat = max(stat - value, 0)
    return max(stat - value, 0)

def loose_stats(stats, values):
    for stat in values:
        loose_stat(stats[stat], values[stat])


'''
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
'''