import random

friends = ["Sandeep", "Shailja", "Monu", "Guar", "Negi"]
# bill = random.choice(friends) THis one way of choosing random names from a list
print("It's time to pay the bill for the food. cards in a bowl will be choosen randomly.")
index = random.randint(0,4)
bill = friends[index]
print(f"{bill} Card was randomly choosen. So {bill} will pay the bills")