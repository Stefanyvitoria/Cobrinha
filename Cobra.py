class snake():
    def __init__(self, master):
        self.master = master
        self.tail = (100,100)
        #self.head = (100,100)
        self.len = 5
        self.body =None#  [None]*self.len

    def draw_Snake(self):
        self.body = self.master.create_rectangle(self.tail,(self.tail[0]+10,self.tail[1]+10), tag='snake', fill='black')


    def move_Left(self):
        self.tail = (self.tail[0]-10, self.tail[1])
        #print(f"moveu left")

    def move_Right(self):
        self.tail = (self.tail[0]+10, self.tail[1])
        #print(f"moveu Right")
    
    def move_Up(self):
        self.tail = (self.tail[0], self.tail[1]-10)
        #print(f"moveu up")
    
    def move_Donw(self):
        self.tail = (self.tail[0], self.tail[1]+10)
        #print(f"moveu down")