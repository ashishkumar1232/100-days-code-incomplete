# from turtle import Turtle,Screen
# ashish=Turtle()
# ashish.shape("turtle")
# ashish.color("blue")
# ashish.forward(120)
# ashish.left(90)
# # ashish.right(90)
# ashish.forward(125)

# screen=Screen()
# screen.exitonclick()
# ---------------------------SQUARE PROJECT---------------------------------------
# from turtle import Turtle,Screen
# tom=Turtle()
# for _ in range(4):
#     tom.forward(190)
#     tom.left(90)
# # tom.forward(190)
# # tom.left(90)
# # tom.forward(190)
# # tom.left(90)
# # tom.forward(190)
# screen=Screen()
# screen.exitonclick()
# ------------------------------USING PENUP AND PENDOWN----------------------------
# from turtle import Turtle,Screen
# tom=Turtle()
# for i in range(15):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()
# screen=Screen()
# screen.exitonclick()
# ----------------------SHAPES WITH RANDOM COLORS----------------------------------
# from turtle import Turtle,Screen
# import random
# tom=Turtle()
# colours=["blue","red","orange","green","yellow"]
# def draw_shapes(num_sides):
#     angle=360/num_sides
#     for i in range(num_sides):
#         tom.forward(100)
#         tom.right(angle)
# for shape_size in range(3,11):
#     tom.color(random.choice(colours))
#     draw_shapes(shape_size)
# screen=Screen()
# screen.exitonclick() 
# -------------------------RANDOM WALK -----------------------------------------
# from turtle import Turtle,Screen
# import random
# tom=Turtle()
# tom.width(10)
# tom.speed("fastest")
# walk=[0,90,180,270]
# colours=["blue","red","orange","green","yellow","black"]
# for i in range(100):
#     tom.forward(15)
#     tom.color(random.choice(colours))
#     tom.setheading(random.choice(walk))
# screen=Screen()
# screen.exitonclick()
# --------------------------RANDOM WALK WITH RANDOM COLOR------------------------
# # from turtle import Turtle,Screen
# import turtle as t
# import random
# tom=t.Turtle()
# tom.width(15)
# t.colormode(255)
# tom.speed("fastest")
# walk=[0,90,180,270]
# # colours=["blue","red","orange","green","yellow","black"]
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     random_color=( r, g, b)
#     return random_color
# for i in range(300):
#     tom.forward(20)
#     tom.color(random_color())
#     tom.setheading(random.choice(walk))
# # screen=Screen()
# # screen.exitonclick()
# ------------------------SPIROGRAPH DRAWING-----------------------------------
import turtle as t
from turtle import Screen
import random
tom=t.Turtle()
t.colormode(255)
tom.speed("fastest")
# tom.width(15)
def random_color():
     r=random.randint(0,255)
     g=random.randint(0,255)
     b=random.randint(0,255)
     random_color=( r, g, b)
     return random_color
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading()+size_of_gap)
draw_spirograph(4)
screen=Screen()
screen.exitonclick()
# -----------------------------------------------------------------------------