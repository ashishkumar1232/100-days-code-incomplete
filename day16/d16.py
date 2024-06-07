# ------------------IMPORTING TURTLE-----------------------------------------------
# from turtle import Turtle,Screen
# tom=Turtle()
# print(tom)
# tom.shape("turtle")
# tom.color("blue")
# tom.forward(100)
# my_screen=Screen()    
# print(my_screen.canvheight)
# my_screen.exitonclick() 
# ---------------------------------------------------------------------------------
from prettytable import PrettyTable
table = PrettyTable()#----->this is the object . 
table.add_column("Pokemon",["pikachu","charmender","sqartle"]) 
table.add_column("type",["electric","fire","water"])
table.align = "l"
print(table)
