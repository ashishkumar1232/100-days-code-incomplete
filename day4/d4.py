# ------------------------RANDOMIZATION AND PYTHON LIST----------------------------
import random
ran_integer=random.randint(1,20)
print(ran_integer)
# # random float number 
# ran_float=random.random()
# print(ran_float)
# ------------------------------------------------------------------------------
# -----------------------HEADS AND TAILS -------------------------------------
# import random
# # list=['heads','tails']
# toss=random.randint(0,1)
# if toss==0:
#     print("tails")
# else:
#     print("heads")
# ---------------------------------------------------------------------------------
# ---------------------------APPEND---"ADDED TO THE LAST OF THE LIST"-----------
# list=["ashish","krish","shubham","prakhar","yuvraj"]
# list.append("smritish")
# list.extend(["tushar","rohan"])
# list.insert(1,"rohit")
# list.remove("ashish")
# list.pop()
# # list.clear()

# print(list)
# -----------------EXTEND---WILL EXTEND THE LIST FROM THE LAST------------------
# -----------------INSERT---WILL INSERT AN ELEMENT TO ANY POSITION-------------
# -----------------REMOVE---REMOVE THE FIRST ITEM FROM LIST---------------------
# -----------------POP---IT WILL POP ELEMENT FROM LAST------------------------
# -----------------DELETE---IT WILL DELETE THE ITEMS SELECTED----------------
# -----------------------------------------------------------------------------------------------------
# --------------------------------RANDOM--CHOICE---------------------------------------------------
# import random 
# list1 = [1, 2, 3, 4, 5, 6] 
# print(random.choice(list1)) 
# # prints a random item from the string 
# string = "striver"
# print(random.choice(string)) 
# -------------------------------------------------------------------------------------------------------
# -------------------------------WITHOUT RANDOM --------------------------------------------------------
# import random
# string1=["ashish","krish","shubham","prakhar"]
# names=string1.split(",")
# item=len(names)
# ch=random.randint(0,item-1)
# who=names[ch]
# ------------------------------------------------------------------------------------------------------
# -------------------------DIRTY DOZEN-----------------------------------------------------------------
# fruit=["Strawberries","Apples","Grapes","Peaches","Cherries","Pears"]
# vegetables=["Potatoes","Tomatoes","Nectarines","Spinach","Kale","Celery"]
# both=[fruit,vegetables]
# print(both)
# print(both[1][3])
# ----------------------------------------------------------------------------------------------------
# -----------------------------TYPE X TO HIDE TREASURE PROJECT-----------------------------------------
# line1=["o","o","o"]
# line2=["o","o","o"]
# line3=["o","o","o"]
# map=[line1,line2,line3]
# print("hiding your treasure : x marks the spot.")
# position=input()
# letter=position[0].lower()
# abc=["a","b","c"]
# letter_index=abc.index(letter)
# number_index=int(position[1])-1
# map[number_index][letter_index]="x"
# print(f"{line1}\n{line2}\n{line3}")
