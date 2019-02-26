from tkinter import *
import time
import tkinter.messagebox

def exit():
    root.destroy()

def create_figure(game):
    canvas.create_rectangle(20, 20, 100, 120)

def start_game(event):
    root.destroy()
    game = Tk()
    game.geometry("800x600")
    game.tkraise()

    game.bind("<space>", create_figure(game))






def move_figure(event):
    canvas.move(1,5,0)

root = Tk()
root.geometry("800x600")
root.title("Hürdenlauf")
root.resizable(0, 0)

# root.bind("<space>", space_click)
root.bind("<Left>", create_figure)
root.bind("<Right>", move_figure)

# start_btn = Button(root, text="Start Game")
# start_btn.bind("<Button-1>", start_game)
#
# end_btn = Button(root, text="Quit", fg="Red", command=exit)

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()



# start_btn.pack()
# end_btn.pack()
root.update()


class Player:
    def __init__(self, canvas, hurdle):
        self.canvas = canvas
        self.hurdle = hurdle
        self.id = canvas.create_oval(10, 10, 25, 25, fill="Red")
        self.canvas.move(self.id, 150, 274)
        self.x = 0
        self.y = -1
        self.canvas.bind_all("<space>", self.jump)
        self.jumping = False

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if self.hit_hurdle(pos):
            print("Hit")


    def jump(self, event):
        self.jumping = True

    def draw_jump(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] < 200:
            self.y = 1
        if pos[3] >= 299:
            self.jumping = False
            self.y = -1

    def hit_hurdle(self, player_pos):
        hurdle_pos = self.canvas.coords(self.hurdle.id)
        if player_pos[2] >= hurdle_pos[0] and player_pos[3] >= hurdle_pos[1] and player_pos[0] <= hurdle_pos[2]:
            time.sleep(0.5)
            return True
        else:
            return False

class Lane:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_line(0, 300, 800, 300)

class Hurdle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 25, 25, fill="Black")
        self.canvas.move(self.id, 450, 274)
        self.x = -1
        self.y = 0

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 1
        if pos[2] > 500:
            self.x = -1

hurdle = Hurdle(canvas)
player = Player(canvas, hurdle)
lane = Lane(canvas)


while 1:
    player.draw()
    hurdle.draw()
    if player.jumping:
        player.draw_jump()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
