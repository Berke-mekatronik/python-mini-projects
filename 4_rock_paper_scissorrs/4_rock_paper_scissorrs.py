rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

choice = int(choice)

if choice == 0:
  print(rock)

if choice == 1:
  print(paper)

if choice == 2:
  print(scissors)

print("Computer choose:")
comp_choice = random.randint(1,2)
if comp_choice == 0:
  print(rock)

if comp_choice == 1:
  print(paper)

if comp_choice == 2:
  print(scissors)

if choice == 0 and comp_choice == 0:
  print("Nobody win")

if choice == 0 and comp_choice == 1:
  print("You lose")

if choice == 0 and comp_choice == 2:
  print("You win")

if choice == 1 and comp_choice == 0:
  print("You win")

if choice == 1 and comp_choice == 1:
  print("Nobody win")

if choice == 1 and comp_choice == 2:
  print("You lose")

if choice == 2 and comp_choice == 0:
  print("You lose")

if choice == 2 and comp_choice == 1:
  print("You win")

if choice == 2 and comp_choice == 2:
  print("Nobody win")