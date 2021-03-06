"Football Formation Board using Python Turtle by Devashish Prasad"

import turtle
wn=turtle.Screen()
wn.title("Football Formation Board")
skk=turtle.Turtle()
skk.hideturtle()

# ---Football Pitch---

skk.penup()
skk.right(90)
skk.forward(20)
skk.left(90)
skk.pendown()
skk.circle(20)
skk.penup()
skk.goto(-70,0)
skk.pendown()
skk.forward(140)
skk.penup()
skk.goto(-70,-110)
skk.pendown()
skk.forward(140)
skk.left(90)
skk.forward(220)
skk.left(90)
skk.forward(140)
skk.left(90)
skk.forward(220)
skk.penup()
skk.left(90)
skk.goto(44,-110)
skk.pendown()
skk.left(90)
skk.forward(36)
skk.left(90)
skk.forward(88)
skk.left(90)
skk.forward(36)
skk.penup()
skk.goto(-44,110)
skk.pendown()
skk.forward(36)
skk.left(90)
skk.forward(88)
skk.left(90)
skk.forward(36)

#------------------The End----------------------

#---Formation Circles---

# Goalkeeper
skk.penup()
skk.goto(5,-92)
skk.pendown()
skk.fillcolor("red")
skk.begin_fill()
skk.circle(5)
skk.end_fill()

# Cente-Backs
skk.penup()
skk.goto(-17,-64)
skk.pendown()
skk.fillcolor("yellow")
skk.begin_fill()
skk.circle(5)
skk.end_fill()
skk.penup()
skk.goto(27,-64)
skk.pendown()
skk.fillcolor("yellow")
skk.begin_fill()
skk.circle(5)
skk.end_fill()

# Full-Backs
skk.penup()
skk.goto(-55,-47)
skk.pendown()
skk.fillcolor("yellow")
skk.begin_fill()
skk.circle(5)
skk.end_fill()
skk.penup()
skk.goto(65,-47)
skk.pendown()
skk.fillcolor("yellow")
skk.begin_fill()
skk.circle(5)
skk.end_fill()

# Holding-Midfielders 
skk.penup()
skk.goto(-31,-10)
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
skk.circle(5)
skk.end_fill()
skk.penup()
skk.goto(41,-10)
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
skk.circle(5)
skk.end_fill()

# Attacking-Midfielder
skk.penup()
skk.goto(5,30)
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
skk.circle(5)
skk.end_fill()

# Wingers
skk.penup()
skk.goto(-55,47)
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
skk.circle(5)
skk.end_fill()
skk.penup()
skk.goto(65,47)
skk.pendown()
skk.fillcolor("green")
skk.begin_fill()
skk.circle(5)
skk.end_fill()

# Striker
skk.penup()
skk.goto(5,64)
skk.pendown()
skk.fillcolor("blue")
skk.begin_fill()
skk.circle(5)
skk.end_fill()

#----------------------------The End-----------------

turtle.done()

