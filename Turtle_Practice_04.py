
import turtle

s = turtle.getscreen()
t=turtle.Turtle()

print("start")

for x in range(7):
  base_length = 5
  length = base_length + ( 2 * x )
  
  t.forward(base_length)
  t.right(50)  
  t.left(length)
  t.forward(length)
  t.forward(base_length)
  t.forward(base_length)
  t.right(length)
  t.circle(10)
  t.forward(50)
  t.circle(10)
  t.left(5)
  t.right(5)
  t.forward(15)
  t.circle(10)
  
"""  
t.right(10)
t.forward(10)
t.circle(5)
t.forward(75)
t.circle(100)
t.right(25)
t.forward(100)
t.circle(5)
t.circle(10)
t.circle(15)
t.circle(20)
t.circle(25)
t.circle(30)
t.circle(35)
t.circle(40)
t.right(50)
t.forward(50)
t.circle(15)
t.circle(20)
t.circle(25)
t.circle(30)
t.right(10)
t.circle(35)
t.circle(40)
t.circle(45)
t.circle(50)
t.right(25)
t.forward(50)
t.circle(45)
t.circle(50)
t.circle(55)
t.circle(60)
t.right(150)
t.circle(100)
t.circle(110)
t.circle(120)
t.circle(115)
t.circle(105)
"""

      