import turtle

s = turtle.getscreen()
t = turtle.Turtle()

"""
seeing if you did two three digit numbers
"""

for x in range(6):
  base_length = 50
  length = base_length * 2
  
  t.right(200)
  t.forward(base_length)
  
  t.right(100)
  t.forward(length)