from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "black", "yellow", "violet", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for c in self.all_cars:
            c.backward(self.car_speed)

    def increase_speed(self):
        self.speed(self.car_speed)
        self.car_speed += MOVE_INCREMENT
