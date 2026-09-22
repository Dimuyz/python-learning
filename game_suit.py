import time
import random

operator = ["rock","paper","scissor"]
print("===== Rock-Paper-Scissors Game =====")
print("there`s a rock, paper and scissor")
print("you may pick a thing")
print("your opponent was an a computer")
computer = random.choice(operator)
player = input("your answer: ")

if computer == player:
    print(f"damn it`s a tie computer and player")
elif (player == "rock" and computer == "scissor") or \
    (player == "paper" and computer == "rock") or \
    (player == "scissor" and computer == "paper"):
    print(f"player won pick a {player}, and computer lose pick a {computer}") 
else:
    print(f"computer won pick a {computer} and player lose pick a {player}")