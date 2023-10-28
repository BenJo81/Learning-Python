from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")
bidding = {}
bidders = 'yes'

while bidders == 'yes':
  name = input("What is your name? ")
  bid = int(input("What is your bid?: $"))
  bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  bidding[name] = bid
  clear()

highest_name = ""
highest_score = 0

for names in bidding:
  if bidding[names] > highest_score:
    highest_name = names
    highest_score = bidding[names]

print(f"The winner is {highest_name} with a bid of ${highest_score}")
  
# dictionaries practice
# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.",
#   "Function": "A piece of code that you can easily call over and over again.",
#   "Loop": "The action of doing something over and over again.",
# }

# print(programming_dictionary["Bug"])

# # Adding new items to a dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# # Creating an empty dictionary and wiping a dictionary
# empty_list = []
# empty_dictionary = {}

# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."

# # Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

# # nesting practice
# {
#   Key: [List],
#   Key2: {Dict},
# }

# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
# }

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# # Nest Dictionary in a Dictionary
# travel_log = {
#   "France" = {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_listed": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }

# # Nesting a Dictionary in a List
# travel_log = [
#   {
#     "country": "France", 
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12
#   },
#   {
#     "country": "Germany", 
#     "cities_listed": ["Berlin", "Hamburg", "Stuttgart"], 
#     "total_visits": 5
#   }
# ]

