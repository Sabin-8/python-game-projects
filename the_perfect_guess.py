import random

random_num=random.randint(1,100)
# print(random_num)         #If i print this then random numbers will be shown and it will be cheating.

user=None
guesses=0

while (user!=random_num):
    user=int(input("Enter your number:\t"))
    guesses+=1
    if user==random_num:
        print("You have guessed it right!")

    else:
        if (user>random_num):
            print("You have guessed it wrong! Enter a smaller number.")
        else:
            print("You have guessed it wrong! Enter a larger number.")
    guesses+=1

print(f"You guessed the number in {guesses} guesses.")

with open ("hiscore.txt","r") as f:
    hiscore=int(f.read())

if (guesses<hiscore):
    print("You have broken the hiscore!")
    with open ("hiscore.txt","w") as f:
        f.write(str(guesses))







