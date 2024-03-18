import random

print("Rock, Paper, Scissors game")
points = 0
attempts = 0
print("Your points: ", points)
print("To quit, type 'q' ")

choices = ["rock", "paper", "scissors"]


while True:

  p1 = input("Enter your choice : ")
  bot = random.choice(choices)
  print("Computers choice : " + bot)
  
  if p1 == choices[0] and bot == choices[1]:
    print("Computer wins")
    attempts += 1
  elif p1 == choices[1] and bot == choices[2]:
    print("Computer wins")
    attempts += 1
  elif p1 == choices[2] and bot == choices[0]:
    print("Computer wins")
    attempts += 1
  elif p1 == choices[2] and bot == choices[1]:
    points += 1
    print("You won! Total points = ", points)
    attempts += 1
  elif p1 == choices[1] and bot == choices[0]:
    points += 1
    print("You won! Total points = ", points)
    attempts += 1
  elif p1 == choices[0] and bot == choices[2]:
    points +=1
    print("You won! Total points = ", points)
    attempts += 1
  elif p1 == bot:
    print("Draw")
    attempts += 1
  elif p1 == "q":
    print("Thanks for playing..... Your points: ", points, ", Your attempts: ", attempts)
    attempts += 1
    break
  else:
    print("Invalid input")
    attempts += 1
