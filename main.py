import tkinter as tk


class Game(tk.Tk):

    def start_game(self):
        pass

    mw = tk.Tk()

    mw.option_add("*Button.Background", "grey")
    mw.option_add("*Button.Foreground", "white")

    mw.title('Hürdenlauf')

    mw.geometry("1000x600")
    mw.resizable(0, 0)

    back = tk.Frame(master=mw)
    back.pack_propagate(0)
    back.pack(fill=tk.BOTH, expand=1)

    go = tk.Button(master=back, text='Start Game', command=start_game)
    go.pack()

    close = tk.Button(master=back, text='Quit', command=mw.destroy)
    close.pack()

    mw.mainloop()


