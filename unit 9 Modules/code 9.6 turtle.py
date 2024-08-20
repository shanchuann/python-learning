import turtle, time
pen = turtle.Turtle()
pen.speed(0)
# for i in range(4):
#     pen.forward(100)
#     pen.right(90)
# pen.write("Hello, world!", font=("Arial", 16, "normal"))
while True:
    time.sleep(1)
    pen.clear()
    pen.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), font=("Arial", 16, "normal"))

