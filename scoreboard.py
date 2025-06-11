from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(self.score, move=False, align="center", font=("Courier", 80, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def l_win(self):
        self.color("white")
        self.goto(0, 0)
        self.write("Congratulations! The left player won!", move=False, align="center", font=("Arial", 18, "normal"))

    def r_win(self):
        self.color("white")
        self.goto(0, 0)
        self.write("Congratulations! The right player won!", move=False, align="center", font=("Arial", 18, "normal"))

