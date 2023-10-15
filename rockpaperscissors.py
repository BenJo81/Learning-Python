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

#Write your code below this line 👇
import random

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
computer_choice = random.randint(1, 3)

if player_choice == "0":
  print(rock)
elif player_choice == "1":
  print(paper)
elif player_choice == "2":
  print(scissors)

print("Computer chose:")

if computer_choice == 1:
  print(rock)
elif computer_choice == 2:
  print(paper)
elif computer_choice == 3:
  print(scissors)

if player_choice == "0" and computer_choice == 1:
  print("Tie game")
if player_choice == "0" and computer_choice == 2:
  print("You lose")
if player_choice == "0" and computer_choice == 3:
  print("You win")
if player_choice == "1" and computer_choice == 1:
  print("You win")
if player_choice == "1" and computer_choice == 2:
  print("Tie game")
if player_choice == "1" and computer_choice == 3:
  print("You lose")
if player_choice == "2" and computer_choice == 1:
  print("You lose")
if player_choice == "2" and computer_choice == 2:
  print("You win")
if player_choice == "2" and computer_choice == 3:
  print("Tie game")
