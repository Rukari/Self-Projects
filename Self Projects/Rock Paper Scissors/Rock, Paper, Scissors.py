#rock paper scissors
import random
import time
pick = ["rock", "scissors", "paper"]
po = random.randint(0, 2)
p = pick[po]
w = "You win"
l = "You lose"
d = "It's a Draw






def game():
    time.sleep(1)
    print("")
    op = input("pick between rock, paper, scissors: ").strip().lower()
    if op == "rock":
        time.sleep(0.5)
        print("You picked", op)
        time.sleep(1)
        print("Opponent picking....")
        time.sleep(2)
        print("Your opponent picked", p)
        time.sleep(1)
        if p == "paper":
            print(l)
        elif p == "scissors":
            print(w)
        else:
            print(d)
    elif op == "paper":
        time.sleep(0.5)
        print("You picked", op)
        time.sleep(1)
        print("Opponent picking....")
        time.sleep(2)
        print("Your opponent picked", p)
        time.sleep(1)
        if p == "scissors":
            print(l)
        elif p == "rock":
            print(w)
        else:
            print(d)
    elif op == "scissors":
        time.sleep(0.5)
        print("You picked", op)
        time.sleep(1)
        print("Opponent picking....")
        time.sleep(2)
        print("Your opponent picked", p)
        time.sleep(1)
        if p == "rock":
            print(l)
        elif p == "paper":
            print(w)
        else:
            print(d)
    else:
        print("That's not in the choices")
    time.sleep(1)
    again()
def again():
    a = input("Do you want to play again y/n: ").strip().lower()
    if a == "y":
        game()
    elif a == "n":
        print("See you later")

game()




    
