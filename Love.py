import turtle

def draw_layer(color, y_position, radius):
    turtle.penup()
    turtle.goto(0, y_position)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_text(text, y_position, text_color):
    turtle.penup()
    turtle.goto(0, y_position)
    turtle.pendown()
    turtle.color(text_color)
    turtle.write(text, align="center", font=("Arial"))

screen = turtle.Screen()
screen.bgcolor("pink")

draw_layer("blue", -200, 150)
draw_text("THE WORLD TO ME", -180, "yellow")

draw_layer("yellow", -50, 150)
draw_text("YOU MEAN", -25, "red")

draw_layer("lightblue", 100, 90)
draw_text(" BABYNISH", 120, "purple")

turtle.penup()
turtle.goto(0, 150)
turtle.setheading(0)
turtle.pendown()
turtle.color("red")

for _ in range(8):  
    turtle.forward(70)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.backward(70)
    turtle.right(45)

turtle.penup()
turtle.goto(0, 250)
turtle.pendown()
turtle.color("purple")
turtle.write("Code_with_Savannah", align="center", font=("Arial"))

turtle.hideturtle()
turtle.done()

