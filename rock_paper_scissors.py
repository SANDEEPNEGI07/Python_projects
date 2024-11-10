import random

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
scissor = ''' _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock,paper,scissor]
user = int(input("What do you choose? Type 0 for rock , 1 for paper or 2 for scissor\n"))
if user >=0 and user <=2:
    print(game_image[user])

computer = random.randint(0,2)
print("computer chooses:")
print(game_image[computer])

if user >=3 or user <0:
    print("You typed an invalid number")

elif user == 0 and computer == 2:
    print("User win")

elif computer == 0 and user == 2:
    print("You lose")

elif computer > user:
    print("you lose")

elif user > computer:
    print("you win")

elif computer == user:
    print("Draw")

