class Hero(object):
    def __init__(self,h,p):
        self.health = h
        self.power = p
        self.name="hero"

    def attack(self,foe):
        foe.health -=self.power
        print "You do %d damage to the %s." %(self.power,foe.name)
        if foe.health <=0:
            print "The %s is dead" % foe.name


class Goblin(object):
    def __init__(self,h,p):
        self.health = h
        self.power = p
        self.name = "goblin"

    def attack(self,foe):
        foe.health -= self.power
        print "The %s does %d damage to you." % (self.name, self.power)
        if foe.health <= 0:
            print "You are dead."
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    hero = Hero(10,5)
    goblin = Goblin(6,2)

    while goblin.health > 0 and hero.health> 0:
        print "You have %d health and %d power." % (hero.health, hero.power)
        print "The %s has %d health and %d power." % (goblin.name,goblin.health, goblin.power)
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            hero.attack(goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin.health > 0:
            goblin.attack(hero)

main()
