import random
# this code is for the user to select the option
print("choose 1.rock ,2.paper , 3.scissor")
choose=int(input("enter the choice : \n" ))
if choose==1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)    rock
      (____)
---.__(___)
""")
elif choose==2:
    print("""
     _______
---'    ____)____
           ______)
          _______)  paper
         _______)
---.__________)
""")
elif choose==3:
     print("""
    _______
---'   ____)____
          ______)
       __________) scissor
      (____)
---.__(___)
""")
else:
    print("wrong input")
    
# this is for the computer point of view
list=[1,2,3]
choic=random.choice(list)
# print(choic)
if choic==1:
    print("""
    _______
---'   ____)
      (_____)
      (_____)    rock
      (____)
---.__(___)
""")
elif choic==2:
    print("""
     _______
---'    ____)____
           ______)
          _______)  paper
         _______)
---.__________)
""")
elif choic==3:
    print("""
    _______
---'   ____)____
          ______)
       __________) scissor
      (____)
---.__(___)
""")
    
# comparision for the both of them for the final result
if(choose==choic):
    print("its a tie ")
elif(choose==1 and choic==2 ):
    print("computer won")
elif(choose==1 and choic==3 ):
    print("you won")
elif(choose==2 and choic==1):
    print("you won")
elif(choose==2 and choic==3 ):
    print("computer won")
elif(choose==3 and choic==1 ):
    print("computer won")
elif(choose==3 and choic==2 ):
    print("you won")