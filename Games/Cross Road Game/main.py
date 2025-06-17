from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600,600)
screen.title("Cross Road Game")
screen.tracer(0)

timmy = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(timmy.go_up, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(timmy) < 25:
            score.game_over()
            is_game_on = False

    if timmy.is_at_finishline():
        timmy.go_to_start()
        car_manager.increase_speed()
        score.increase_level()
screen.exitonclick()