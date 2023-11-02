from art import logo
from art import vs
from game_data import data
from replit import clear
import random
game_on = True
score = 0

# Function to randomly select a person from the list
def selection():
  person = random.choice(data)
  return person

# Function to set up the game
def game_set_up():
  person_a = selection()
  person_b = selection()
  if person_a == person_b:
    person_b = selection()
  return person_a, person_b

def compare(person_a, person_b):
  if person_a['follower_count'] > person_b['follower_count']:
    winner = "a"
  else:
    winner = "b"
  return winner

person_a, person_b = game_set_up()

while game_on:
  print(logo)
  if score > 0:
    print(f"You're right! Current score: {score}")

  print(f"Compare A: {person_a['name']}, {person_a['description']}, {person_a['country']}")
  print(vs)
  print(f"Against B: {person_b['name']}, {person_b['description']}, {person_b['country']}")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  # Compare to see who has more followers
  winner = compare(person_a, person_b)
  if answer == winner:
    person_a = person_b
    person_b = selection()
    if person_a == person_b:
      person_b = selection()
    score += 1
    clear()
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    game_on = False