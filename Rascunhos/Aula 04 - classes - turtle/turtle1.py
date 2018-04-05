# Programa para desenhar um quadrado #
#                                    #
#                                    #

import turtle

def draw_square():
    zeca = turtle.Turtle()
    zeca.shape("turtle")
    zeca.color("yellow")
    zeca.speed("normal")

    nsides = 4

    for n in range(0, nsides):
        zeca.forward(100)
        zeca.right(90)

def draw_circle():
    zoca = turtle.Turtle()
    zoca.shape("turtle")
    zoca.color("green")
    zoca.speed("normal")

    zoca.circle(100)

def draw_triangle():
    zana = turtle.Turtle()
    zana.shape("square")
    zana.color("green")
    zana.speed("normal")

    for n in range(0,3):
        zana.forward(100)
        zana.right(60)

window = turtle.Screen()
window.bgcolor("blue")
draw_triangle()
draw_square()
draw_circle()


window.exitonclick()
