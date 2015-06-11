#!/bin/python

import effects

class Tourment:
    name = 'Tourment'
    text = '5 dmg'

    @staticmethod
    def cast(target =None, t =text):
        if effects.deal_dmg(target, dmg=5):
            print t
            return True
        return False

###########################
###  SKILL=>NAME TABLES ###
###########################

skill_table = {
    Tourment: 'Tourment'
}
'''
    'Cri': 1,
    'Morsure': 5,
    'Charge': 5,
    'Fireball': 10,
    'Iceball': 10,
    'Energy Shot': 15

}


class Skill:
    def __init__(self, name, dmg, descr):
        self.name = name
        self.dmg = dmg
        self.descr = descr

tourment = Skill('Tourment', 2, 'Leave me!')
cri = Skill('Cri', 1, 'Kiyaa!')
morsure = Skill('Morsure', 5, 'Peste!')
charge = Skill('Charge', 5, 'Here I Come')

fireball = Skill('Fireball', 10, 'It burns')
iceball = Skill('Iceball', 10, 'It freezes')
energyshot = Skill('Energy Shot', 15, 'It hurts')
'''