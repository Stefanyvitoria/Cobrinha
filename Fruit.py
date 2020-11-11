import random
class fruit():
    def __init__(self, master):
        self.master = master
        
        self.x = None
        self.y = None 

        self.new_aplle()
        
    def draw_Aplle(self):
        self.master.create_oval(self.x, self.y, self.x+10, self.y+10, tag='aplle', fill='red')
    
    def new_aplle(self, snake=[]):
        self.master.delete('aplle')
        self.x = random.randint(0,49)*10
        self.y = random.randint(0,49)*10
        self.coord_aplle = (self.x, self.y,self.x+10, self.y+10)

        self.draw_Aplle()
    
