import time
import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state = []
while len(guessed_state) < len(data.state):
    time.sleep(0.1)
    screen.update()

    answer_state = screen.textinput(title= f"{len(guessed_state)}/50",
                                    prompt= "What's another states name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)

        df = pandas.DataFrame(missing_state)
        df.to_csv("states_to_learn.csv")

        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        timmy = Turtle()
        timmy.penup()
        timmy.hideturtle()
        state_data = data[data.state == answer_state]
        timmy.goto(state_data.x.item(), state_data.y.item())
        timmy.write(answer_state)




screen.exitonclick()



# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()