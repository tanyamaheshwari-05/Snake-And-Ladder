import random

print("Welcome to Sanke and Ladder game")

position1 = 0
print("Start Position of Player 1: ",position1)

count=0

def roll_dice():
    dice=random.randint(1, 6)
    return dice


def option_choose():
    options=["No play","Snake","Ladder"]
    return random.choice(options)

while position1<100:
    dice= roll_dice()
    option=option_choose()
    count+=1

    if(option=="No play"):
        print("Player stays at the same position : ",position1)

    elif (option=="Ladder"):
        if position1 + dice <= 100 :
            position1+=dice
        print("Player move forward:", position1)

    elif(option=="Snake"):
        position1-=dice
        if(position1<0):
            position1=0
        print("Snake Bite! Position of player:", position1)
print("Total dice rolled:", count)