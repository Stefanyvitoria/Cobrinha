class snake():
    def __init__(self, master):
        self.master = master
        self.head = (100,100,110,110)
        self.len = 3
        self.body =[None]*self.len
        self.draw_Snake()

    def draw_Snake(self, Aux='L'):
        if Aux == 'L' or Aux == 'R':
            for i in range(self.len):
                self.body = self.master.create_rectangle((self.head[0]+(10*i), self.head[1]), (self.head[2]+(10*i),self.head[3]), tag='snake')#, fill='black')
        elif Aux == 'U' or Aux == 'D':
            for i in range(self.len):
                self.body = self.master.create_rectangle((self.head[0], self.head[1]+(10*i)), (self.head[2],self.head[3]+(10*i)), tag='snake')#, fill='black')

    def move_Left(self):
        self.head = (self.head[0]-10, self.head[1], self.head[2]-10, self.head[3])
        self.draw_Snake('L')

    def move_Right(self):
        self.head = (self.head[0]+10, self.head[1], self.head[2]+10, self.head[3])
        self.draw_Snake('R')
    
    def move_Up(self):
        self.head = (self.head[0], self.head[1]-10, self.head[2], self.head[3]-10)
        self.draw_Snake('U')
    
    def move_Donw(self):
        self.head = (self.head[0], self.head[1]+10, self.head[2], self.head[3]+10)
        self.draw_Snake('D')
