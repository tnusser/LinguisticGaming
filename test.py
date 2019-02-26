from tkinter import *
import tkinter as tk


# class Game(tk.Tk):
#
#     def start_game(self):
#         pass
#
#     mw = tk.Tk()
#
#     mw.option_add("*Button.Background", "grey")
#     mw.option_add("*Button.Foreground", "white")
#
#     mw.title('Hürdenlauf')
#
#     mw.geometry("1000x600")
#     mw.resizable(0, 0)
#
#     back = tk.Frame(master=mw)
#     back.pack_propagate(0)
#     back.pack(fill=tk.BOTH, expand=1)
#
#     go = tk.Button(master=back, text='Start Game', command=start_game)
#     go.pack()
#
#     close = tk.Button(master=back, text='Quit', command=mw.destroy)
#     close.pack()
#
#     mw.mainloop()

#
# class Test():

root = Tk()
root.title("Hürdenlauf")
# tk.Button(root, text="Hello").grid()
# #
# frame = Frame(root)
# labelText = StringVar()
# label = Label(frame, textvariable=labelText)
# button = Button(frame, text="Click me")
# labelText.set("I am a label")
#
# label.pack()
# button.pack()

# frame = Frame(root)
# Label(frame, text="This is a sample text").pack()
# Button(frame, text="Button1").pack(side=LEFT, fill=Y)
# Button(frame, text="Button2").pack(side=TOP, fill=X)
# Button(frame, text="Button3").pack(side=RIGHT, fill=X)
# Button(frame, text="Button4").pack(side=LEFT, fill=X)

# Label(root, text="First name").grid(row=0, sticky=W, padx=10)
# Entry(root).grid(row=0, column=1, sticky=E, pady=4)
#
# Label(root, text="Last name").grid(row=1, sticky=W, padx=10)
# Entry(root).grid(row=1, column=1, sticky=E, pady=4)
#
# Button(root, text="Submit").grid(row=3, column=1)

# frame.pack()

# Label(root, text="Description").grid(row=0, column=0, sticky=W)
# Entry(root, width=50).grid(row=0, column=1)
# Button(root, text="Submit").grid(row=0, column=8)
#
# Label(root, text="Quality").grid(row=1, column=0, sticky=W)
# Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
# Radiobutton(root, text="Good", value=2).grid(row=3, column=0, sticky=W)
# Radiobutton(root, text="Poor", value=3).grid(row=4, column=0, sticky=W)
# Radiobutton(root, text="Damaged", value=4).grid(row=5, column=0, sticky=W)
#
# Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
# Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
# Checkbutton(root, text="Bonus gift").grid(row=3, column=1, sticky=W)
# Checkbutton(root, text="Free Shipping").grid(row=4, column=1, sticky=W)

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 + num2
    sumEntry.insert(0, sum)

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

button = Button(root, text="=")
button.bind("<Button-1>", get_sum)
button.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()