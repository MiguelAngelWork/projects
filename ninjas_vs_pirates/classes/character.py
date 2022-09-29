import random

class Character:

    def __init__( self , name, strength, speed, health ):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , enemy ):
        rand = random.randint(1,10)
        enemy.health -= self.strength+rand
        print(f'{self.name} attacked {enemy.n}')
        return self