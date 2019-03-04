from tkinter import *
import time
import random


class Background:
    """
    Class for objects in the background of the game
    """

    def __init__(self, canvas):
        """
        Init method for initializing objects
        :param canvas: for drawing objects
        """
        self.canvas = canvas
        self.canvas.create_line(0, m.height / 2, m.width, m.height / 2)


class Hurdle:
    """
    Class for the individual hurdles
    """

    def __init__(self, canvas, speed):
        """
        Init method for initializing attributes of hurdle
        :param canvas: canvas for drawing the hurdle
        :param speed: value for the speed of a hurdle
        """
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 25, 25, fill="Black")
        self.canvas.move(self.id, 800, 274)
        self.x = speed
        self.y = 0

    def draw(self):
        """
        Draw method which is in charge of positioning a hurdle
        :return:
        """
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] < 100:
            if self.id not in m.hurdle_stack.passed_hurdles:
                m.hurdle_stack.passed_hurdles.append(self.id)
            self.canvas.game_score = m.hurdle_stack.passed_hurdles.__len__()


class HurdleStack:
    """
    Stack of created hurdles
    """

    def __init__(self, canvas):
        """
        Init method for initializing attributes for the hurdle stack
        :param canvas:
        """
        self.canvas = canvas
        self.hurdle_list = [Hurdle(canvas, -2)]
        self.next_hurdle_index = 0
        self.passed_hurdles = []

    def create_hurdle(self):
        """
        Method which generates new hurdles onto the hurdlestack if a previous hurdle passes a certain border on the lane
        :return:
        """
        if self.canvas.coords(self.hurdle_list[self.next_hurdle_index].id)[2] < self.generate_spawn_pos():
            if self.canvas.game_score < 10:
                speed = -2.5
                self.increase_speed(speed)
            elif self.canvas.game_score < 20:
                speed = -3
                self.increase_speed(speed)
            elif self.canvas.game_score < 30:
                speed = -3.5
                self.increase_speed(speed)
            elif self.canvas.game_score < 40:
                speed = -4
                self.increase_speed(speed)
            elif self.canvas.game_score < 50:
                speed = -4.5
                self.increase_speed(speed)
            else:
                speed = -5
                self.increase_speed(speed)
            self.hurdle_list.append(Hurdle(self.canvas, speed))
            self.next_hurdle_index += 1

    def increase_speed(self, speed):
        """
        Method which increases the speed of the hurdles currently on the game
        :param speed: parameter of the speed
        :return:
        """
        for hurdle in self.hurdle_list:
            hurdle.x = speed

    def generate_spawn_pos(self):
        """
        Generates a random border value to specify if a new hurdle can be created yet
        :return:
        """
        return random.randint(400, 650)


class Player:
    """
    Class of the player (red ball)
    """

    def __init__(self, canvas):
        """
        Init method for initializing attributes for the player such as position, speed, jumping characteristics etc
        :param canvas:
        """
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill="Red")
        self.canvas.move(self.id, 150, 274)
        self.x = 0
        self.y = -3.5
        self.canvas.bind_all("<space>", self.jump)
        self.jumping = False
        self.hit = False

    def draw(self):
        """
        Drawing method for the player
        :return:
        """
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        for hurdle in m.hurdle_stack.hurdle_list:
            if self.hit_hurdle(pos, hurdle):
                self.hit = True
                self.canvas.create_text(200, 200, text="Game over")

    def jump(self, event):
        """
        Event handler for the jump action. If users presses 'space' the player jumps
        :param event:
        :return:
        """
        self.jumping = True

    def draw_jump(self):
        """
        Method which draws creates the jump animation
        :return:
        """
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] < 225:
            self.y = 3
        if pos[3] >= 299:
            self.jumping = False
            self.y = -3.5

    def hit_hurdle(self, player_pos, hurdle):
        """
        Method which checks for collisions with hurdles
        :param player_pos: position of the player
        :param hurdle: position of a hurdle
        :return:
        """
        hurdle_pos = self.canvas.coords(hurdle.id)
        if player_pos[2] >= hurdle_pos[0] and player_pos[3] >= hurdle_pos[1] and player_pos[0] <= hurdle_pos[2]:
            return True
        else:
            return False


def loop(hurdle_stack, player):
    """
    Main loop for the hurdling game
    :param hurdle_stack: stack of hurdles currently generated
    :param player: instance of the player
    :return:
    """
    while m.existing:
        if m.start:
            if not player.hit:
                player.draw()
                hurdle_stack.create_hurdle()
                for hurdle in hurdle_stack.hurdle_list:
                    hurdle.draw()
                if player.jumping:
                    player.draw_jump()

            m.canvas.itemconfig(m.score_obj, text=m.canvas.game_score)
        m.root.update_idletasks()
        m.root.update()
        time.sleep(0.01)


class Menu:
    """
    Class for the game menu
    """

    def __init__(self):
        """
        Init method which sets attributes and creates buttons
        """
        self.game = Tk()
        self.game.geometry("800x600")
        self.game.update()

        start_btn = Button(self.game, text="Start Game")
        start_btn.bind("<Button-1>", self.start_game)
        end_btn = Button(self.game, text="Quit", fg="Red", command=self.exit)
        start_btn.pack()
        end_btn.pack()
        self.start = False
        self.exit = False
        self.root = None
        self.width = 900
        self.height = 600
        self.canvas = None
        self.score_obj = None
        self.hurdle_stack = None
        self.game_bg = None
        self.existing = True

    def exit(self):
        """
        Exit method which destroys the menu window
        :return:
        """
        self.exit = True
        self.game.destroy()

    def start_game(self, event):
        """
        Method which switches from menu to game itself and generates all the object instances
        :param event:
        :return:
        """
        self.game.destroy()
        self.root = Tk()
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.geometry("800x600")
        self.root.title("Hürdenlauf")
        self.root.resizable(0, 0)

        self.canvas = Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.canvas.game_score = 0
        self.canvas.pack()
        self.score_obj = self.canvas.create_text(100, 100, text=self.canvas.game_score, font=("Comic Sans", 50))
        self.start = True

        self.game_bg = Background(m.canvas)
        self.hurdle_stack = HurdleStack(m.canvas)
        player = Player(m.canvas)
        loop(self.hurdle_stack, player)


"""
Instantiates menu
"""
m = Menu()
while not m.start and not m.exit:
    m.game.update_idletasks()
    m.game.update()
    time.sleep(0.01)
