from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.refresh_food()


    def refresh_food(self):
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(rand_x,rand_y)
    


            
