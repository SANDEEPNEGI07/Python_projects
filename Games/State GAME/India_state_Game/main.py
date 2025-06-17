import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("India States Game")
img = "India_map.gif"
screen.addshape(img)
turtle.shape(img)
screen.tracer(0)

data = pandas.read_csv("state_coordinates.csv")
all_state = data.state.to_list()
guessed_state = []
while len(guessed_state) < len(data.state):
    screen.update()

    answer_state = screen.textinput(title= f"{len(guessed_state)}/{len(all_state)}",
                                    prompt= "What's another states name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_state if state not in guessed_state]

        df = pandas.DataFrame(missing_state)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_state and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        timmy = Turtle()
        timmy.penup()
        timmy.hideturtle()
        state_data = data[data.state == answer_state]
        timmy.goto(state_data.x.item(), state_data.y.item())
        timmy.write(answer_state)


screen.exitonclick()