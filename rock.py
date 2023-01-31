import random

print("0 for rock, 1 for papper, 2 for scissor:")
user = int(input("enter your choice:"))
computer = random.randint(0, 2)
if user > 2:
    print("please choose the number between 0,1,2")
else:

    if (user == computer):
        print("draw")
    elif ((user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1)):
        print("you win👏👏👏👏👏😊")
    else:
        print("computer win😒😒😒😒")
print("computer",computer)