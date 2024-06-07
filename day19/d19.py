# from turtle import Turtle, Screen
# tom=Turtle()
# screen=Screen()
# def move_forward():
#     tom.forward(10)
# screen.listen()
# screen.onkey(key="space",fun=move_forward)
# screen.exitonclick()
# --------------------------CHALLANGE 1-------------------------------------
from turtle import Turtle, Screen
tom=Turtle()
screen=Screen()
def move_forward():
    tom.forward(10)
def move_backward():
    tom.backward(10)
def turn_left():
   new_heading= tom.heading()+10
   tom.setheading(new_heading)
def turn_right():
   new_heading= tom.heading()-10
   tom.setheading(new_heading)
def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()