import turtle

s = turtle.getscreen()
t = turtle.Turtle()
"""
"""
for x in range(3):
  base_length = 70
  length=base_length * 3
  t.right(90)
  t.left(length)
  t.forward(base_length)
  print(90-length)

t.circle(20)