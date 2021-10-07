class Weapon:

    def __init__(self, name, attack_power):
       self.name= name
       self.weapon_power= attack_power
       self.weapon_list=[]
       self.create_weapon()

    def create_weapon(self):
        wep_one= Weapon('laser pointer', 5)
        wep_two= Weapon('stun blaster', 4)
        wep_three= Weapon('dim saber', 3)
        self.weapon_list.append(wep_one)
        self.weapon_list.append(wep_two)
        self.weapon_list.append(wep_three)
        