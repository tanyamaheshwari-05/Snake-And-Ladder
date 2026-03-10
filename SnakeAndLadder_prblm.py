import random

print("Welcome to Sanke and Ladder game")

position1 = 0
print("Start Position of Player 1: ",position1)


def roll_dice():
    dice=random.randint(1, 6)
    return dice


def option_choose():
    options=["No play","Snake","Ladder"]
    return random.choice(options)

while p1<100:
    dice= roll_dice()
    option=option_choose()

    if(option=="No play"):
        print("Player stays at the same position : ",position1)

    elif (option=="Ladder"):
        position1+=dice

    elif(option=="Snake"):
        position1-=dice
        if(position1<0):
            position1=0
print("Player reached 100 and win!")
