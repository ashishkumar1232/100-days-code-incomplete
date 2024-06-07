# import tkinter  --> if we write this we will have to write Tkinter in function to call
from tkinter import * #-->this will import everything 
window=Tk()
window.title("first GUI")
window.minsize(width=500,height=300)
my_label=Label(text="i am a label",font=("Arial",24,"bold"))
my_label.pack()
my_label["text"]="new label" # this is for the changing the character of the text 

def button_click():
    print("I got clicked ")
    new_text=input.get(text="write something to get started")
    my_label.config(text=new_text)


                       #button
button =Button(text="click me ", command=button_click)
# my_label.config(text="click me ")  #this is for the changing the character of the text .tis is second method
button.pack()# --> we can replace this into the bracket (side="left")



                    #entry
input= Entry()
input.pack()
print(input.get())

window.mainloop()
# ----------------------------------------------------------------------------
# --------------------ARGS ----------------------------------------------------
# def add(*args):
#     print(args[0])
#     sum=0
#     for i in args:
#         sum +=i
#     return sum
# print(add(1,2,3,4,5,6,9,7,88,8,6,4,5,6,4,3,4,6,8,56565,4,4545,3))

# # ----------kwargs---------------------------------
# def calculate(n,**kwargs):
#     print(kwargs)
#     # for key,value in kwargs.items():
#     #     print(key)
#     #     print(value)

#     n+=kwargs["add"] #-> THIS IS THE FIRST TYPE TO DECLARE 
#     n*=kwargs["multiply"] # --> TIS IS SECOND METHOD.
#     print(n)
# calculate(2,add=3,multiply=5)
# # ---------------------------------CLASS -------------------
# class car:
#     def __init__(self,**kw):
#         self.make=kw["make"]
#         self.model=kw.get("model")
#         self.colour=kw.get("colour")
#         self.seats=kw.get("seats")
# my_car=car(make="Tata",model="jeep")
# print(my_car.seats)
# --------------------------------------------------------------------------------------------------------