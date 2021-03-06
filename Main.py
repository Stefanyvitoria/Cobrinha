import tkinter, Snake, time, Fruit

class main():
    def __init__(self, master):
        self.master = master
        self.master.title("Snake game - Stefany Izidio.")
        self.master.geometry("550x550")
        
        self.titulo = tkinter.Label(self.master, text='Snake Game!')
        self.titulo.pack()

        self.canvas = tkinter.Canvas(self.master,width=500, height=500, bg='#008000')
        self.canvas.pack() 

        self.score = 0
        self.label_Score = tkinter.Label(self.master, text=f'Score: {self.score}')
        self.label_Score.pack() 

        self.Snake = Snake.snake(self.canvas) #Create snake
        self.fruit = Fruit.fruit(self.canvas) #Create fruit
        
        self.end = False #Aux

        #Bind
        self.canvas.focus_force()
        self.canvas.bind("<KeyPress>", self.play)

        self.master.mainloop()

    def play(self, event = None):

        if event.keysym == 'Left':
            self.Snake.move_Left() #Move
            if self.Snake.detect_Collision(): self.game_Over() #Collision        
            self.snake_Eat_aplle() #Check collision aplle

        elif event.keysym == 'Right':
            self.Snake.move_Right()
            if self.Snake.detect_Collision(): self.game_Over()
            self.snake_Eat_aplle()

        elif event.keysym == 'Up':
            self.Snake.move_Up()
            if self.Snake.detect_Collision(): self.game_Over()
            self.snake_Eat_aplle()

        elif event.keysym == 'Down':
            self.Snake.move_Donw()
            if self.Snake.detect_Collision(): self.game_Over()
            self.snake_Eat_aplle()

        elif event.keysym == 'BackSpace':
            self.master.quit() 

        elif event.keysym == 'Return' or event.keysym == 'KP_Enter':
            self.canvas.delete('end')
            self.Snake = Snake.snake(self.canvas)
            self.fruit = Fruit.fruit(self.canvas)
            self.label_Score.destroy()
            self.score = 0
            self.label_Score = tkinter.Label(self.master, text=f'Score: {self.score}')
            self.label_Score.pack()
        else:
            pass
    
    def game_Over(self):
        self.label_End = self.canvas.create_text(255,220, text= f"Game over!\n Score: {self.score}", tag='end')
        self.canvas.delete('snake')
        self.canvas.delete('aplle')

    def snake_Eat_aplle(self):
        if self.fruit.coord_aplle == self.Snake.head:
            #Score
            self.label_Score.destroy()
            self.score += 1
            self.label_Score = tkinter.Label(self.master, text=f'Score: {self.score}')
            self.label_Score.pack()
            #Update            
            self.fruit.new_aplle()
            self.Snake.add_Snake()
            
                

if __name__ == '__main__':
    master = tkinter.Tk() 
    snake = main(master)
    
