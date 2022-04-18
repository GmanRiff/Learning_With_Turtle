
import turtle

s = turtle.getscreen()
t=turtle.Turtle()

for x in range (50):
 base_length = 5
 length = base_length + 5
 t.left(base_length)
 t.forward(length)
t.left(175)
t.forward(100)
t.left(200)
t.circle(150)