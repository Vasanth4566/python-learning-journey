print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the 'Legendary Pirate Treasure'.")
print("You arrive at Skull Island searching for pirate gold.")
option1=(input("There are two paths in front of you. Do you walk through the forest or along the beach? Type:L for left option and R for right option "))
if option1 == "R":
    option2 = (input("A pirate ship suddenly appears near the shore.Do you hide behind the trees or attack the pirates? Type:L for left option and R for right option"))
    if option2 == "L":
        option3 = (input("The pirates do not notice you. After they leave, you find a secret map leading to hidden treasure.You follow the map and discover three treasure chests:gold, silver, and black. what will you choose? type the tressure you want to choose"))
        if option3 == "gold":
            print("You open the gold chest and find the Pirate King's treasure.YOU WIN!")
        elif option3 == "silver":
            print("You open the silver chest.It is completely empty.GAME OVER.")
        else:
            print("You open the black chest.A deadly curse is released.GAME OVER.")
    else:
        print("You are dead. Game Over!")

else:
    print("You enter the dark forest filled with strange noises. Game Over!")






