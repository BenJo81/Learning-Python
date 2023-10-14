print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input("You awaken to find yourself on a small desert island. You aren't sure how you got there. What do you do first? Type \"check pockets\" or \"do a cartwheel\"\n")
if choice1.lower() == "check pockets":
  choice2 = input("You find an old treasure map and aren't quite sure how it ended up in your pocket. You notice the map indicates a larger island due South and you turn around to see that it is close by. You notice there is a boat. Do you take the boat or swim? Type \"boat\" or \"swim\"\n")
  if choice2.lower() == "boat":
    choice3 = input("You safely arrive at the larger island. The map indicates there is treasure close by marked with a big \"X\". You travel to the \"X\" marked on the map and discover three caves in the wall of a mountain. Which do you enter? Type \"cave 1\", \"cave 2\", or \"cave 3\"\n")
    if choice3.lower() == "cave 1":
      print("You slowly enter the pitch black cave and here a faint rattle. As you go further into the darkness it gets louder. You are attacked by a den on snakes. You do not survive. Game over.")
    elif choice3.lower() == "cave 2":
      print("You move further and further into the darkness of the cave. You trip over something and discover it is a treasure chest. You open the chest and discover pirate gold. You win!")
    else:
      print("You enter the dark cave and the air feels cool and empty. You keep moving further into the cave and fall into a deep pit. You do not survive. Game over.")
  else:
    print("You begin swimming towards the island and realize this was a poor decision. The map is ruined and you are being hunted by sharks. You do not survive. Game over.")
else:
  print("You try to perform a cartwheel but you collapse under the weight of your own body. You do not survive. Game over.")