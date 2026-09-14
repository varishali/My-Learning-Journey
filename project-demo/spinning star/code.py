import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spinning Star")

t = turtle.Turtle()
t.speed(0)
t.color("yellow")

for i in range(100):
    t.forward(100)
    t.right(144)
    t.right(1)

screen.exitonclick()