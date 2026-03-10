import random

print("Welcome to Sanke and Ladder game")

position1 = 0
print("Start Position of Player 1: ",position1)

def roll_dice():
    dice=random.randint(1, 6)
    return dice


