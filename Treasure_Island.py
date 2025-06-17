print('''Welcome to Treasure Island 
Your mission is to find the treasure''')

choice_1 = input('''You're at a cross road. Where do you want to go?
Type "Left" or "Right" \n''').lower()

if choice_1 == 'left':
    choice_2 = input('''You have came across an seashore
        Do you want to "swim" or "wait"?\n''').lower()
    
    if(choice_2 == 'wait'):
        choice_3 = input(''' You have reached to the Castle of an Island. Which door do you want to go IN? "red", "yellow", "blue"?\n''').lower()
        if(choice_3 == "yellow"):
            print("Congratulations you won!!")
        
        elif choice_3 == "blue":
            print("Game Over. You enter a room full of snakes.")
        elif choice_3 == "red":
            print('''Game Over. You are attacked by the Lion ''')
        else:
            print("You have choose the wrong Door. Game Over")
    else:
        print('''You've been attacked by a Shark. Game Over''')
# # elif:
#     print('''You've been attacked by a ferocious beast''')
elif choice_1=="right":
    print("You fell into a Hole. Game Over.")

else:
    print("You enter the Wrong Direction. Game Over")