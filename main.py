import random

print("Rock, Paper, Scissors game")

choices = ["rock", "paper", "scissors"]

p1 = input("Enter your choice : ")
bot = random.choice(choices)

if p1 == choices[0] and bot == choices[1]:
  print("Computer wins")
elif p1 == choices[1] and bot == choices[2]:
  print("Computer wins")
elif p1 == choices[2] and bot == choices[0]:
  print("Computer wins")
elif p1 == choices[2] and bot == choices[1]:
  print("You won!")
elif p1 == choices[1] and bot == choices[0]:
  print("You won!")
elif p1 == choices[1] and bot == choices[0]:
  print("You won!")
elif p1 == bot:
  print("Draw")
else:
  print("Invalid input")

print("Computers choice : " + bot)