import turtle
from turtle import Screen
import pandas as pd

screen = Screen()
img = "India_map.gif"
screen.addshape(img)
turtle.shape(img)

states_of_india = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# Data storage for state name and coordinates
state_data = []

# Function to get coordinates when clicked
def click_on_state(x, y):
    # Ask for state name after clicking
    state_name = screen.textinput("Enter State Name", "Which state is this?")
    if state_name:
        state_data.append({"State": state_name, "x": x, "y": y})
        print(f"Saved: {state_name} → ({x}, {y})")

screen.onscreenclick(click_on_state)
screen.mainloop()

df = pd.DataFrame(state_data)
df.to_csv("state_coordinates.csv", index=False)
print("Saved all state coordinates!")


