import turtle
window = turtle.Screen()
window.bgcolor("#1735ad")
turtle_pen = turtle.Pen()
turtle_pen.pencolor("#36eb42")
for counter in range(100):
    turtle_pen.circle(counter)
    turtle_pen.left(257)
