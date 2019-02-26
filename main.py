from tkinter import *
import time
import random
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
    canvas.move(1, 5, 0)


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
width = 900
height = 600
canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
canvas.pack()

# start_btn.pack()
# end_btn.pack()
root.update()


class Player:
    def __init__(self, canvas, hurdle):
        self.canvas = canvas
        self.hurdle = hurdle
        self.hurdle_list = []
        self.id = canvas.create_oval(10, 10, 25, 25, fill="Red")
        self.canvas.move(self.id, 150, 274)
        self.x = 0
        self.y = -2
        self.canvas.bind_all("<space>", self.jump)
        self.jumping = False
        self.hit = False

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if self.hit_hurdle(pos):
            self.hit = True
            self.canvas.create_text(200, 200, text="Game over")

    def jump(self, event):
        self.jumping = True

    def draw_jump(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] < 200:
            self.y = 2
        if pos[3] >= 299:
            self.jumping = False
            self.y = -2

    def hit_hurdle(self, player_pos):
        hurdle_pos = self.canvas.coords(self.hurdle.id)
        if player_pos[2] >= hurdle_pos[0] and player_pos[3] >= hurdle_pos[1] and player_pos[0] <= hurdle_pos[2]:
            return True
        else:
            return False


class Hurdle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 25, 25, fill="Black")
        self.canvas.move(self.id, 450, 274)
        self.x = -2
        self.y = 0

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 2
        if pos[2] > 500:
            self.x = -2


class Background:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_line(0, height / 2, width, height / 2)


lane = Background(canvas)
hurdle = Hurdle(canvas)
player = Player(canvas, hurdle)


while 1:
    if not player.hit:
        player.draw()
        player.hurdle.draw()
        if player.jumping:
            player.draw_jump()
    curr_hurdle_pos = canvas.coords(player.hurdle.id)
    if curr_hurdle_pos[2] < canvas.coords(player.id)[0] - 10:
        canvas.delete(player.hurdle.id)
        player.hurdle = Hurdle(canvas)
        player.hurdle.draw()

    root.update_idletasks()
    root.update()
    time.sleep(0.01)
