
from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
from robot import Robot



class Battlefield:

    def __init__(self):
        self.herd= Herd()
        self.fleet= Fleet()
        self.run_game()
        
                
        
        
    def run_game(self):
         self.trex= self.herd.dinosaurs[0]
         self.spino= self.herd.dinosaurs[1]
         self.allo= self.herd.dinosaurs[2]
         self.robo_one= self.fleet.robots[0]        
         self.robo_two= self.fleet.robots[1]
         self.robo_three= self.fleet.robots[2]
         print(self.trex.name)


         self.dispaly_welcome()
         self.dino_turn(Dinosaur)
         self.robo_turn(Robot)
        
        
        
        
        

    def dispaly_welcome(self):
        print('Welcome to Dinosaurs vs Robots')

    def battle(self):
        print('Pick "1" to play as Dinosaurs, Pick "2" to play as Robots')
        user= input()
        if user == 1:
           print('Player picked Team Dinosaur')
        elif user == 2:
            print('Player picked Team Robot')

        # while health != 0
        # robo attack then dino attack
        #     if health = 0
        #         for dino in dinosaurs
        #             new dinosaur

    def dino_turn(self, Dinosaur):
        

        self.trex.attack_power

        

        # dinosaur.attack- robot.health= robot.heath
        pass
        

        
        
        
        
    def robo_turn(self, robot):
        # robot.attack- dinosaur.health= dinosaur.health
        # print(f' Robot {robot} is attacking!')
           
        
        pass



    def show_dino_opponet_options(self):
        self.fleet.robots[0]        
        self.fleet.robots[1]
        self.fleet.robots[2]

    def show_robo_opponent_options(self):
        self.trex= self.herd.dinosaurs[0]
        self.spino= self.herd.dinosaurs[1]
        self.allo= self.herd.dinosaurs[2]

    def display_winner(self):
        pass












