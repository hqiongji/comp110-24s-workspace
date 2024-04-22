"""TODO: Draw the star, people, sun and Tree."""
 
__author__ = "730719415"
 
import turtle

def draw_star(t, x, y, length)-> None:
    """Draw stars."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()

def draw_person(t, x, y)-> None:
    """Draw person."""
    # Head
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(10)
    
    # Body
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.forward(20)
    
    # Arms
    t.penup()
    t.goto(x, y - 15)
    t.pendown()
    t.left(45)
    t.forward(15)
    t.penup()
    t.back(15)
    t.right(90)
    t.pendown()
    t.forward(15)
    t.right(45) 

def draw_branch(t, branch_length)-> None:
    """Draw a tree's branch."""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(t, branch_length - 15)
        t.left(40)
        draw_branch(t, branch_length - 15)
        t.right(20)
        t.backward(branch_length)

def draw_tree(t, x, y, trunk_height)-> None:
    """Draw a tree's trunk."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.right(90)
    t.forward(trunk_height)
    draw_branch(t, trunk_height)

def draw_sun(t, x, y, radius)-> None:
    """Draw a sun."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def main()-> None:
    """To set up the scene"""
    window = turtle.Screen()
    window.bgcolor("lightblue")

    leo = turtle.Turtle()
    leo.color("yellow")
    leo.fillcolor("yellow") #info from the google for fillling the shape

    draw_sun(leo, 100, 100, 50)
    
    leo.color("green")
    draw_tree(leo, -200, -150, 60)
    
    leo.fillcolor("blue")
    draw_person(leo, 0, -100)
    draw_person(leo, 50, -100)
    
    leo.color("red")
    draw_star(leo, -100, 50, 40)

    turtle.done()

if __name__ == "__main__":
    main()