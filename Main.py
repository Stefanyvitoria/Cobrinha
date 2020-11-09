import tkinter, Cobra, time

class screen():
    def __init__(self, master):
        self.master = master
        self.master.title("Snake game - Stefany Izidio.")
        self.master.geometry("550x550+1300+250")
        
        self.titulo = tkinter.Label(self.master, text='Snake Game!')
        self.titulo.pack()

        self.canvas = tkinter.Canvas(self.master,width=500, height=500, bg='#476042')
        self.canvas.pack() 

        self.score = 0
        self.label_Score = tkinter.Label(self.master, text=f'Score: {self.score}')
        self.label_Score.pack() 

        self.Snake = Cobra.snake(self.canvas)
        #self.Snake.draw_Snake()

        self.end = False


        #Bind
        self.canvas.focus_force()
        self.canvas.bind("<KeyPress>", self.play)

        self.master.mainloop()

    def play(self, event = None):

        self.canvas.delete('snake')

        if event.keysym == 'Left':
            self.Snake.move_Left()
        elif event.keysym == 'Right':
            self.Snake.move_Right()
        elif event.keysym == 'Up':
            self.Snake.move_Up()
        elif event.keysym == 'Down':
            self.Snake.move_Donw()
        else:
            self.master.quit()
        
        
        #self.canvas.delete('snake')
        #self.Snake.draw_Snake()

if __name__ == '__main__':
    master = tkinter.Tk() 
    snake = screen(master)
    
