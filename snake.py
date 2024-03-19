from turtle import *

# Define the starting positions for the snake segments
shape_list = [(0, 0), (-15, 0), (-30, 0)]


Left = 180
Right = 0
Up = 90
Down =270

class Snake:
    def __init__(self):
        self.segments = []  # Use a more descriptive name
        self.create_snake()
        self.head = self.segments[0] 

    def create_snake(self):
        for position in shape_list:
            self.add_segment(position)  # Append to segments list

    def add_segment(self,position):
        new_segment = Turtle("circle")
        new_segment.color("Green")
        new_segment.shapesize(0.75,0.75)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment) 

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor() 
            self.segments[i].goto(new_x, new_y)
        self.head.forward(15)

    def left(self):    
        if self.head.heading() != Right:
            self.head.setheading(Left) 

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right) 

    def up(self):
        if self.head.heading() != Down :
            self.head.setheading(Up)


    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down) 
                

            