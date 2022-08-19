from random import *
from tkinter import *

window = Tk()

def rock():
    lists=['rock','paper','scissors']
    while True:
        random = choice(lists)
        print(random)
        bokk = "rock"
        if bokk=="rock" and random=="scissors":
            print("You won")
            break
        elif bokk==random:
            print("draw")
            break
        elif random=="paper" and bokk=="rock":
            print("computer wins")
            break
def paper():
    lists=['rock','paper','scissors']
    while True:
        random = choice(lists)
        print(random)
        bokk = "paper"
        if bokk=="paper" and random=="rock":
            print("You won")
            break
        elif bokk==random:
            print("draw")
            break
        elif random=="scissors" and bokk=="paper":
            print("computer wins")
            break
def scissors():
    lists=['rock','paper','scissors']
    while True:
        random = choice(lists)
        print(random)
        bokk = "scissors"
        if bokk=="scissors" and random=="paper":
            print("You won")
            break
        elif bokk==random:
            print("draw")
            break
        elif random=="rock" and bokk=="scissors":
            print("computer wins")
            break
rock = Button(window,text="rock",command=rock)
rock.pack()

paper=Button(window,text="paper",command=paper)
paper.pack()

scissors =Button(window,text="scissors",command=scissors)
scissors.pack()

quit = Button(window,text="quit",command=quit)
quit.pack()
window.mainloop()
