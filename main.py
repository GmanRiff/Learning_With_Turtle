import turtle

s = turtle.getscreen()
t = turtle.Turtle()

print("start")
for x in range(72):
    base_length = 5
    length = base_length + 5
    t.left(base_length)
t.forward(length)
t.forward(100)
t.right(50)
t.forward(50)
t.right(30)
t.forward(50)
t.right(5)