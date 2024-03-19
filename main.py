from turtle import Screen ,write
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("My Snake Game")
screen.setup(600,600)

screen.bgcolor("black")
screen.tracer(0)  # tracer is off - Turn turtle animation on/off and set delay for update drawings 

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 10:
        food.refresh_food()
        snake.extend()
        scoreboard.calculate_score()

    #Detect colliosn with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10: #here it checks the distance between head of snake with remaing
            game_is_on =False                       #parts if it is less than 10 then it meants head get collied with its own body
            scoreboard.game_over()


screen.exitonclick()
 