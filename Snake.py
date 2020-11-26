class snake():
    def __init__(self, master):
        self.master = master

        #Snake config
        self.head = (100,100,110,110)
        self.len = 3
        self.snake_Body =[None]*self.len
        self.coord_snake = []

        #Var auxiliary
        self.tmp = None
        self.tmp1 = None

        self.draw_Snake('I') #Draw first

    def draw_Snake(self, Aux=None):
        if Aux == 'I':
            self.snake_Body[0] = self.master.create_rectangle(self.head, tag='snake', fill='black') #Draw the head
            for i in range(1,self.len):
                self.snake_Body[i] = self.master.create_rectangle((self.head[0]+(10*i), self.head[1]), (self.head[2]+(10*i),self.head[3]), tag='snake', fill='#006600')#Draw the body
                self.coord_snake.append(self.master.coords(self.snake_Body[i]))
        else:
            self.coord_snake = []
            self.master.itemconfig('snake', tag="snake_old") #old snake

            self.tmp = self.master.coords(self.snake_Body[0])
            for i in range(1,self.len): #Draw the body
                self.tmp1 = self.master.coords(self.snake_Body[i])
                self.snake_Body[i] = self.master.create_rectangle(self.tmp,  tag='snake',fill="#006600")
                self.coord_snake.append(self.tmp)
                self.tmp = self.tmp1
            self.snake_Body[0] = self.master.create_rectangle(self.head,  tag='snake', fill='black') #Draw the head

            self.master.delete('snake_old') #delete old snake


    def move_Left(self):
        self.head = (self.head[0]-10, self.head[1], self.head[2]-10, self.head[3])
        self.draw_Snake()

    def move_Right(self):
        self.head = (self.head[0]+10, self.head[1], self.head[2]+10, self.head[3])
        self.draw_Snake()
    
    def move_Up(self):
        self.head = (self.head[0], self.head[1]-10, self.head[2], self.head[3]-10)
        self.draw_Snake()
    
    def move_Donw(self):
        self.head = (self.head[0], self.head[1]+10, self.head[2], self.head[3]+10)
        self.draw_Snake()

    def add_Snake(self):
        """Add a part in the tail."""
        self.snake_Body.append(None)
        self.snake_Body[-1] = self.master.create_rectangle(self.tmp, tag='snake',fill="#006600")
        self.len += 1

    def detect_Collision(self):
        if list(self.head) in self.coord_snake:
            return True
        elif self.head[0] > 490 or self.head[1] > 490 or self.head[0] < 0 or self.head[1] < 0 :
            return True
        return False