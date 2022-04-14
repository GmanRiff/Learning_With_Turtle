import turtle

s = turtle.getscreen()
t=turtle.Turtle()

print("start")

for x in range(50):
  base_length = 5
  length = base_length + ( 2 * x )
  
  t.forward(base_length)
  t.right(base_length)
  t.forward(base_length)
  t.left(length)
  
  t.forward(base_length)
  t.forward(base_length)
  t.left(length) 
print("end")