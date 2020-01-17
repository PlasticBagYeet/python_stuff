import turtle
window = turtle.Screen()
window.bgcolor("black")
window.title("YEET")
turtle_pen = turtle.Pen()
turtle_pen.pencolor("green")
for counter in range(300000000000):
    turtle_pen.forward(counter)
    turtle_pen.left(146)
    if(counter > 50):
        turtle_pen.pensize(1)
        window.bgcolor("blue")
    else:
        turtle_pen.pensize(2)
        # move this print function in and out of this loop
print("i'm all done!!")