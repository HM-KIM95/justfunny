import turtle
t = turtle.Turtle()
colors = ["red", "blue", "green", "orange", "purple"]

for i in range(6):
    t.color(colors[i])
    for _ in range(5):
        t.forward(100)
        t.right(72)
    t.right(60)
    
turtle.done()