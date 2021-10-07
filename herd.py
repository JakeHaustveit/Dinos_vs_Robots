from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dinosaurs= []
        self.create_herd()
        print(self.dinosaurs)

    def create_herd(self):
        dino_one= Dinosaur('T-rex', 45)
        dino_two= Dinosaur('Spino', 40)
        dino_three= Dinosaur('Allo', 35)
          
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
        
        












