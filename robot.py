from weapon import Weapon

class Robot:

    def __init__(self, name):
       
        self.name= name
        self.health= int(35)
        self.weapon= int(4)

    def attack(self, dinosaur):
        self.weapon

    def pick_weapon(self):
        print(' pick "1" for laser pointer, pick "2" for stun gun, pick "3" for dim saber')
        weapon_choice= input()
        if weapon_choice == 1:
            self.weapon= weapon_choice
        elif weapon_choice == 2:
            self.weapon= weapon_choice
        elif weapon_choice== 3:
            self.weapon= weapon_choice

    def __str__(self) -> str:
        return print(self.name)    