class Fleet:

    def __init__(self):
        self.robots=[]

    def create_fleet(self):
        self.robots.append()



class Robot:

    def __init__(self, name):
        self.name= name
        self.health= 35
        self.weapon= Weapon()

    def attack(self, dinosaur):
        pass


class Weapon:

    def __init__(self, name, attack_power):
       self.name= name
       self.weapon_power= attack_power




robo_1= Robot('beep')
robo_2= Robot('beep boop')
robo_3= Robot('bop')
robo_4= Robot('beep bop')
robo_5= Robot('bop beeb')
robo_6= Robot('borp')
robo_7= Robot('borp beep')
robo_8= Robot('beep borp')
robo_9= Robot('bop borp')
robo_10= Robot('borp bop')
robo_11= Robot('boop borp')
robo_12= Robot('borp boop')
robo_13= Robot('beep boop bop')
robo_14= Robot('bop boop beep')
robo_15= Robot('boop bop beep')
robo_16= Robot('boop beep bop')
robo_17= Robot('bop bop')
robo_18= Robot('beep beep')
robo_19= Robot('boop boop')
robo_20= Robot('borp borp')
robo_21= Robot('steve')
robo_22= Robot('bob')
robo_23= Robot('jeff')




wep_one= Weapon('laser pointer', 5)
wep_two= Weapon('stun blaster', 4)
wep_three= Weapon('dim saber', 3)