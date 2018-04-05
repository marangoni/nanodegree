import turtle

def draw_square(size, ang):

    zeca = turtle.Turtle()
    zeca.shape("turtle")
    zeca.color("yellow")
    zeca.speed("fastest")
    zeca.seth(ang)
    for n in range(0,4):
        zeca.forward(size)
        zeca.right(90)


window = turtle.Screen()
window.bgcolor("blue")

for angle in range(0,360):
    draw_square(100,angle)
    angle = angle + 15



window.exitonclick()
