import random

print("Welcome to Sanke and Ladder game")

position1 = 0
print("Start Position of Player 1: ",position1)
position2=0
print("Start Position of Player 2: ",position2)


count=0
turn =random.choice([1,2])
print("Player " ,turn, " will start the first")

def roll_dice():
    dice=random.randint(1, 6)
    return dice


def option_choose():
    options=["No play","Snake","Ladder"]
    return random.choice(options)

while position1<100 and position2<100:

    dice= roll_dice()
    option=option_choose()
    count+=1

    if(turn==1):
        position = position1
    else:
        position = position2
    print("Player ",turn, " dice ",dice,  " option ",option )

    if(option=="No play"):
        print("Player stays at the same position : ",position1)
        turn=2 if turn ==1 else 1

    elif (option=="Ladder"):
        if position + dice <= 100 :
            position+=dice
        print("Player move forward:", position)

    elif(option=="Snake"):
        position-=dice
        if(position<0):
            position=0
        print("Snake Bite! Position of player:", position)
        turn =2 if turn ==1 else 1
    if(turn ==1):
        position1=position
    else:
        position2=position
    if(position==100):
        print("Player ",turn , " win the match ")
print("Total dice rolled:", count)