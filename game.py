# Game of Rock, Paper, and Scissor!

import random

def game_win(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return False
        elif you=='s':
            return True
    elif comp=='p':
        if you=='s':
            return False
        elif you=='r':
            return True
    elif comp=='s':
        if you=='r':
            return False
        elif you=='p':
            return True

print("Computer's Turn: Rock(r), Paper(p), or Scissor(s)?")
random_no=random.randint(1,3)
if random_no==1:
    comp='r'
elif random_no==2:
    comp='p'
elif random_no==3:
    comp='s'


you=input("Yours Turn: Rock(r), Paper(p), or Scissor(s)?--> ")

a=game_win(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a==None:
    print("It's a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")