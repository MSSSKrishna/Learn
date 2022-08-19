import random


def guess():
    y = random.randint(1,10)
    attempts = 0
    while True:
        try:
            num = int(input("Enter a number(1-10):"))
            if num<1 and num>10:
                raise ValueError("please,give a valid input")
        
        except ValueError as err :
            print(err)
        else:
            if  num <y:
                print("You are less than number")
                attempts +=1
            elif num>y:
                print("You are greater than number")
                attempts +=1
            elif num==y:
                print("Great job!!!! :)")
                attempts +=1
                
        if num==y:
            print("you took {} times to find number:".format(attempts))
            n = input("Do you wanna play again?")
            
            if n.lower() == "yes":
                guess()
            else:
                break
guess()

#!or


