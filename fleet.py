from robot import Robot

class Fleet:

    def __init__(self):
        self.robots=[]
        self.create_fleet()
        print(self.robots)

    def create_fleet(self):
        robo_1= Robot('beep')
        robo_2= Robot('beep boop')
        robo_3= Robot('bop')
        
      
        self.robots.append(robo_1)
        self.robots.append(robo_2)
        self.robots.append(robo_3)
        
      
      


































