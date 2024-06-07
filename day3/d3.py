# -----------------------IF ELSE STATEMENT-------------------------------------

# print("Welcome to the rollercoster.....")
# height=int(input("enter the height in cm ?\n"))
# if height>120:
#     print("you can ride the rollercoster.......")
# else:
#     print("sorry you cannot ride the rollercoster.........")
# ---------------------------------------------------------------------------------
# -----------------ODD OR EVEN----------------------------------------------------
# num=int(input("enter the number ?\n"))
# if num%2==0:
#     print("the number is even ...")
# else:
#     print("the number is odd...")
# -------------------------------------------------------------------------------
# --------------NESTED IF STATEMENT AND ELIF STATEMENT-----------------------------
# print("Welcome to the rollercoster.....")
# height=int(input("enter the height in cm ?\n"))
# if height>120:
#     print("you can ride the rollercoster.......")
#     age=int(input("enter the age ?\n"))
#     if(age>10):
#         print("you can ride ..")
#     else:
#         print("you cannot ride ..")
# else:
#     print("sorry you cannot ride the rollercoster.........")
# --------------------------------------------------------------------------------
# -----------------------NESTED ELIF STATEMENT-----------------------------------
# print("Welcome to the rollercoster.....")
# height=int(input("enter the height in cm ?\n"))
# if height>120:
#     print("you can ride the rollercoster.......")
#     age=int(input("enter the age ?\n"))
#     if(age<10):
#         print("you can ride ..but 150rs")
#     elif age<=18:
#         print("you can ride but 200rs")
#     else:
#         print("you can ride ..but 300rs")
# else:
#     print("sorry you cannot ride the rollercoster.........")
# ---------------------------------------------------------------------------------
# ----------------------BODY MASS INDEX USING ELIF ------------------------------
# height=float(input("enter the height in cm ?"))
# weight=int(input("enter the weight in kg ?"))
# bmi=weight*height**2
# print("the body mass index is ",round(bmi,2))
# if bmi<=18.5:
#     print("the person is underweight.")
# elif bmi<=25:
#     print("the person is of normal weight.")
# elif bmi<=30:
#     print("the person is slightly overweight.")
# elif bmi<=35:
#     print("the person is obuse.")
# else:
#     print("the person is critically obuse.")
# ..----------------------------------------------------------------------------
# ----------------------------LEAP YEAR ------------------------------------------
# year=int(input("enter the year for checking.\n"))
# if year%4==0:
#     if year%100!=0:
#         if year%400==0:
#             print("year is not leap .")
#         else:
#             print("leap year")
#     else:
#         print("not a leap year.")
# else:
#     print("year is not a leap year.")
# ---------------------------------------------------------------------------------
# ---------------------------MULTIPLE IF STATEMENT--------------------------------
# print("Welcome to the rollercoster.....")
# height=int(input("enter the height in cm ?\n"))
# if height>120:
#     print("you can ride the rollercoster.......")
#     age=int(input("enter the age ?\n"))
#     if(age<10):
#         print("you can ride ..but 150rs")
#         bill=150
#     elif age<=18:
#         print("you can ride but 200rs")
#         bill=200
#     else:
#         print("you can ride ..but 300rs")
#         bill=300
# else:
#     print("sorry you cannot ride the rollercoster.........")
# photos=input("enter y/n if photos is required ?")
# if photos=="y":
#     totalbill=bill+30
#     print(totalbill)
# else:
#     totalbill=bill
#     print(totalbill)
# ---------------------------------------------------------------------------------
# -------------------PIZZA QUESTION------------------------------------------
# print("thanks for choosing python pizza deliveries!")
# size=input("enter the size of pizza s/m/l?\n")
# if size=="s":
#     rate=150
# elif size=="m":
#     rate=200
# elif size=="l":
#     rate=250
    
# peproni=input("enter y/n for peproni ?\n")
# if peproni=="y":
#     pepsize=input("enter the size of pizza for peproni s/m/l?\n")
#     if pepsize=="s":
#         rate+=20
#     elif pepsize=="m"or"l":
#         rate+=30
# else:
#     print(rate)
# cheese=input("want extra cheese y/n ?")
# if cheese=="y":
#     rate+=10
# else:
#     print(rate)
# print(f"the total bill is {rate}")
# --------------------------------------------------------------------------------
# ----------------------LOVE CALCULATOR------------------------------------
print("the love calculator is calculating your score...")
name1=input("enter your name ?\n")
name2=input("enter other name ?\n")
combined=name1+name2
low=combined.lower()
t=low.count("t")
r=low.count("r")
u=low.count("u")
e=low.count("e")
first=t+r+u+e

l=low.count("l")
o=low.count("o")
v=low.count("v")
e=low.count("e")
second=l+o+v+e

score=int(str(first)+str(second))
if score<10 or score>90:
    print(f"your score is {score} and you go together like a coke and mentos")
elif score>=40 and score<=50:
    print(f"your score is {score} you are alright together ")
else :
    print(f"your score is {score}")