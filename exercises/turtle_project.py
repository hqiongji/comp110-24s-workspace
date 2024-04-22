"""My Scene is about a dark night with moon, stars, mountains and a small lake."""

__author__: str = "730520183"
import turtle


def star(t: turtle.Turtle, x: float, y: float, size: float, color: str = "yellow") -> None:
    """Draw stars with yellow color."""
    t.color(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def moon(t: turtle.Turtle, x: float, y: float, radius: float) -> None:
    """Lightgray moon using circle."""
    t.color("lightgray")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def mountain(t: turtle.Turtle, x: float, y: float, size: float) -> None:
    """Triangle  mountain."""
    if size < 20:
        return
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.goto(x + size / 2, y + size)
    t.goto(x + size, y)
    t.end_fill()
    mountain(t, x + size / 4, y + size / 2, size / 2)


def lake(t: turtle.Turtle, x: float, y: float, width: float, height: float) -> None:
    """Lake between two mountains."""
    t.color("blue")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.circle(height / 2, 90)
    t.end_fill()


def main() -> None:
    """Main Function for the drawing."""
    screen = turtle.Screen()
    screen.bgcolor("navy")

    scene = turtle.Turtle()
    scene.speed(0)
    scene.hideturtle()

    moon(scene, -200, 100, 50)
    
    star_size = 15
    stars_count = 15
    for i in range(stars_count):
        x = -300 + (i % 5) * 150 
        y = 200 - (i // 5) * 100 
        star(scene, x, y, star_size)

    scene.color("darkgrey")
    mountain(scene, -400, -100, 300)
    mountain(scene, 0, -100, 300)

    lake(scene, -200, -200, 400, 100)

    turtle.done()


if __name__ == "__main__":
    main()
