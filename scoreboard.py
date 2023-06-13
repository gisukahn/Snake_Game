from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0, 250)
        self.write(f"your Score : {self.score}", align="center", font=("Arial", 16, "normal"))
        self.refresh()
        self.penup()
        self.hideturtle()



    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align= 'center', font=("Arial", 16, "normal"))
    def refresh(self):

        self.clear()
        self.write(f"your Score : {self.score}", align="center", font=("Arial", 16, "normal"))
        self.score += 1
        # self.write(f"your Score : {self.score}")
