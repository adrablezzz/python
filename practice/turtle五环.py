import turtle

turtle.width(10)
turtle.color('red')
turtle.circle(50)

turtle.penup()
turtle.goto(110, 0)
turtle.pendown()
turtle.color('yellow')
turtle.circle(50)

turtle.penup()
turtle.goto(-110, 0)
turtle.pendown()
turtle.color('black')
turtle.circle(50)

turtle.penup()
turtle.goto(-55, -50)
turtle.pendown()
turtle.color('green')
turtle.circle(50)

turtle.penup()
turtle.goto(55, -50)
turtle.pendown()
turtle.color('purple')
turtle.circle(50)

turtle.done()
