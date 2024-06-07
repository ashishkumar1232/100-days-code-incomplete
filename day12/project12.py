import random
print("welcome to the number guessing game ")
print("i'm thinking the number between 1 to 100 :")
numbers=random.randint(1,101)
print(numbers)
# num=random.choice(numbers)
choose=input("choose a difficulty level 'easy'=e or 'hard'=h")
write=0
# this is for the easy level of difficulty 
if choose=="e" or "E":
    chance=10
    print(f"you have {chance} chances remaning")
    while(chance!=0):
        for i in range(1,11):
            write=int(input("enter the number :"))
            if numbers==write:
                print("yes you choose the correct answer")
                print("you win ...")
            elif write>numbers:
                print("too high!")
            else:
                print("too low!") 
            chance-=1
            print(f"you have {chance} chances remaning")
            if chance==0:
                print("you loose...")
# this is for the hard level of difficulty
if choose=="h" or "H":
    chances=5
    print(f"you have {chances} chances remaning")
    while(chances!=0):
        for i in range(1,6):
            write=int(input("enter the number :"))
            if numbers==write:
                print("yes you choose the correct answer")
                print("you win ...")
            elif write>numbers:
                print("too high!")
            else:
                print("too low!") 
            chances-=1
            print(f"you have {chances} chances remaning")
            if chances==0:
                print("you loose...")
