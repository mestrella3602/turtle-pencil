from mypolygon import*
import turtle

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

for times in range(255):
    c=(times,0,0)
    bob.forward(times*2)
    bob.left(75)
    bob.forward(2)
    bob.color(0,times,times)
    print(c)
    polygon(bob,3,50)

