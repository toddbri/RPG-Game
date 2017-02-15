"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random , os
import time
delay_scale = 0.0
class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5*delay_scale)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)
        if self.health <= 0:
            print "%s is dead." % self.name

class Dramatic(Character):
    import sys
    def __init__(self):
        self.name = 'dramatic'
        self.health = 20
        self.power = 2
        self.coins = 15
        self.statements =["Oh gosh! that really hurt","wait, wait, wait, give me a few minutes",
                         "Really, you had to do that?", "I'm having a bad day....\n\n\n can we continue this later?",
                         "Please don't hurt me anymore", "How about we stop this and get some coffee?",
                         "give me a few minutes, just gotta finish something up","Damn, that is going to leave a stain"]

    def receive_damage(self,points):
        print "%s says: " % self.name
        Dramatic.sys.stdout.write("\033[1;31m")
        print self.statements[int(random.random()*len(self.statements))].upper()
        Dramatic.sys.stdout.write("\033[0;0m")
        super(Dramatic, self).receive_damage(points)

class Shifter(Character):
    import inspect as Inspector

class Renewer(Character):
    def __init__(self):
        self.name = 'renewer'
        self.health = 3
        self.power = 3
        self.coins = 17

    def receive_damage(self,points):
        renew = random.random() < .7
        if renew:
            print "%s has regenerated." % self.name
            self.__init__()
        else:
            self.health -=points

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.recupe = 2

    def receive_damage(self,points):
        self.health -=points
        print "%s received %d damage." % (self.name, points)
        if ((random.random() < 0.2) and (self.health + self.recupe >0)):
            print "%s has recuperated %d health points." % (self.name, self.recupe)
            self.health +=self.recupe
        if self.health <= 0:
            print "%s is dead." % self.name

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 1
        self.power = 1
        self.coins = 3

    def receive_damage(self,points):
        print "%s can't be killed...." % self.name

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 3
        self.coins = 5

    def receive_damage(self,points):
        if random.random() < 0.1:
            print "%s has avoided your damage.....too bad" % self.name
        else:
            self.health -=points

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

    def attack(self,enemy):
        double_damage = random.random() < 0.2
        if double_damage:
            print "%s has magically doubled damage during this attack" % (self.name)
            self.power *=2
        super(Hero, self).attack(enemy)
        if double_damage:
            self.power /=2

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1*delay_scale)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power and self.alive():
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5*delay_scale)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Chicken."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)
os.system("clear")
hero = Hero()
enemies = [Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero,Dramatic())
    # hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    # shopping_engine.do_shopping(hero)

print "YOU WIN!"
