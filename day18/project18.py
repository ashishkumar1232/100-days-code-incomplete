import turtle as t
from turtle import Screen 
import random
t.colormode(255)
tom=t.Turtle()
tom.penup()
tom.hideturtle()
color_list =["blue","red","orange","green","yellow","black"]
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
tom.speed("fastest")
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tom.dot(20,random.choice(color_list))
    tom.forward(50)

    if dot_count%10==0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)

screen=Screen()
screen.exitonclick()

