import os
class Character(object):
    def __init__(self,h,p,name):
        self.health = h
        self.power = p
        self.name=name

    def alive(self):
        return self.health>0

    def print_status(self):
        print "The %s has %d health and %d power." % (self.name,self.health, self.power)

    def attack(self,foe):
        foe.health -= self.power
        print "The %s does %d damage to you." % (self.name, self.power)
        if not foe.alive():
            print "You are dead."

class Hero(Character):
    def attack(self,foe):
        foe.health -=self.power
        print "You do %d damage to the %s." %(self.power,foe.name)
        if not foe.alive():
            print "The %s is dead" % foe.name

    def print_status(self):
        print "You have %d health and %d power." % (self.health, self.power)

class Goblin(Character):
    pass

class Zombie(Character):
    def alive(self):
        return True

def make_choice(creature):
    print
    print "What do you want to do?"
    print "1. fight %s" % creature.name
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    os.system("clear")
    return input


def main():
    os.system("clear")
    hero = Hero(10,5,"hero")
    goblin = Zombie(1,1,"zombie")
    # goblin = Goblin(6,2,"goblin")

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        input = make_choice(goblin)
        if input == "1": #attack
            hero.attack(goblin)
        elif input == "2": #do nothing
            pass
        elif input == "3": #flee
            print "Chicken!"
            break
        else:
            print "Invalid input %r" % input

        if goblin.alive():
            goblin.attack(hero)

main()
