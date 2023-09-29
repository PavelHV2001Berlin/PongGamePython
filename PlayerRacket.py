from turtle import Turtle

class PlayerRacket(Turtle):
    def __init__(self, startingPosition):
        super().__init__()
        self.startingPosition = startingPosition
        self.yPosition = self.startingPosition[1]
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(self.startingPosition)
        self.shapesize(5,1)
    def up(self):
        self.yPosition += 25
        self.goto(self.startingPosition[0], self.yPosition)
    def down(self):
        self.yPosition -= 25
        self.goto(self.startingPosition[0], self.yPosition)
