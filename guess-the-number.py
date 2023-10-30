#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

guess = 0
life_total = 0
answer = random.randint(1, 100)
print(logo)
print("I'm thinking of a number between 1 and 100.")
print("You'll need to guess my number correctly to win.")

while life_total != 5 and life_total != 10:
  game_difficulty = input("Type 'easy' or 'hard' to select which mode you would like to play: ").lower()
  if game_difficulty == "easy":
    life_total = 10
  elif game_difficulty == "hard":
    life_total = 5
  else:
    print("That was not a valid input. Please try again.")

while life_total > 0 and guess != answer:
  print(f"You have {life_total} guesses remaining.")
  guess = int(input("Guess a number between 1-100: "))
  if guess < answer:
    print("Too low.")
    life_total -= 1
  elif guess > answer:
    print("Too high.")
    life_total -= 1
  elif guess == answer:
    print(f"You win! 🏆 The correct number was {answer}.")
  else:
    print(f"You lose. 😭 The correct number was {answer}.")

print(f"You lose. 😭 The correct number was {answer}.")
