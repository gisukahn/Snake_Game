from turtle import Screen, Turtle
up = 90
down = 270
left = 180
right = 0
class Snake:

    def __init__(self):
        x = 0
        self.segments = []
        for _ in range(3):

            self.gisuk = Turtle()
            self.gisuk.penup()
            self.gisuk.shape("square")
            self.gisuk.color("white")
            self.gisuk.goto(x, 0)
            x -= 20
            self.segments.append(self.gisuk)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def add_segment(self, position):
        self.gisuk = Turtle()
        self.gisuk.penup()
        self.gisuk.shape("square")
        self.gisuk.color("white")
        self.gisuk.goto(position)
        self.segments.append(self.gisuk)


    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != up:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != left:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != right:
            self.segments[0].setheading(180)