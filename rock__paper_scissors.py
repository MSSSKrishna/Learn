from random import *
'''
def p():
    lists = ['rock','paper','scissors']
    uw,cw,no = 0,0,0
    while True:
        random= choice(lists)
        user = input("Enter rock/paper/scissors/q:").lower()
        if random=="rock" and user=="paper":
            print("You won!")
            uw += 1
        elif random=="paper" and user=="scissors":
            print("You won !!!!!")
            uw += 1
        elif random=="scissors" and user=="rock":
            print("you won")
            uw+=1
        elif random=="rock" and user=="scissors":
            print("computer won !!!!!")
            cw += 1
        elif random=="paper" and user=="rock":
            print("computer won")
            cw+=1
        elif random=="scissors" and user=="paper":
            print("computer wins")
            cw+=1
        elif random==user:
            print("draw...")
            no+=1
        elif user=="q":
            print("Computer wins",cw)
            print("User wins",uw)
            print("no results",no)
            break
        else:
            print("wrong input")
p()
'''

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

window.mainloop()


