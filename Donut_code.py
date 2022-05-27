import turtle

s = turtle.getscreen()
t = turtle.Turtle()

print("start")

for x in range(72):
    base_length = 5
    length = base_length + 6
  
    t.right(base_length)
    t.forward(length)
    t.left(length)
    t.forward(base_length)
    t.right(length)
    t.circle(10)
    t.right(base_length)
    t.right(75)   
    t.forward(length)
    t.left(length)
    t.forward(base_length)
    t.right(length)
    t.circle(10)