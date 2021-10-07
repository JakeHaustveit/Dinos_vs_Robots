
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
         self.dino_list= self.herd.dinosaurs       
         self.robo_list= self.fleet.robots       
         
         self.dispaly_welcome()
        
         self.battle()
        
        
        
        
        

    def dispaly_welcome(self):
        print('Welcome to Dinosaurs vs Robots')

    def battle(self):
        trex= self.dino_list[0]
        spino= self.dino_list[1]
        allo= self.dino_list[2]

        robo_1= self.robo_list[0]
        robo_2= self.robo_list[1]
        robo_3= self.robo_list[2]

        print('press 1 to fight with dinosaurs, press 2 to fight with robots.')
        user_input= input()

        if user_input== '1':
            robot_health=300
            while robot_health != 0:

               attacked_health=robot_health
                
            print('press 1 for trex to attack, press 2 for spino to attack, press 3 for allo to attack')
            dino_input= input()
            if dino_input == '1':
                trex.attack_power - robot_health
                return robot_health
            elif dino_input == '2':
                spino.attack_power- robot_health
                return robot_health
            elif dino_input == '3':
                allo.attack_power- robot_health
                return robot_health



        elif user_input == '2':
            dino_health=300
            while dino_health != 0:

                print('press 1 for Beep to attack, press 2 for boop to attack, press 3 for bop to attack')
                robo_input= input()
                if robo_input == '1':
                    robo_1.attack()
                elif robo_input == '2':
                    robo_2.attack()
                elif robo_input == '3':
                    robo_3.attack()
       
           

        
            
            

      

    def dino_turn(self, dinosaur):
        pass

        
        

       
        

        
        
        
        
    def robo_turn(self, robot):
        pass
        
           
        
        



    def show_dino_opponet_options(self):
        print(self.fleet.robots[0])        
        print(self.fleet.robots[1])
        print(self.fleet.robots[2])
        pass

    def show_robo_opponent_options(self):
        print(self.herd.dinosaurs[0])
        print(self.herd.dinosaurs[1])
        print(self.herd.dinosaurs[2])
        pass

    def display_winner(self):
        pass












