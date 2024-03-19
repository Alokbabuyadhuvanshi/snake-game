from turtle import Turtle

Alignment = "center"
Font = ('Comic Sans MS', 24, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over",align= Alignment, font=Font)

    
    def update_score(self):
        self.write(f"Score : {self.score} ", move=False, align=Alignment , font=Font)
    def calculate_score(self):
        self.score +=1
        self.clear()
        self.update_score()



