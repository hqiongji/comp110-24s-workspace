from turtle import Turtle, colormode, done

colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()

leo.color(99, 204, 250)  # This sets both the pencolor and fillcolor
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()


leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()

done()

