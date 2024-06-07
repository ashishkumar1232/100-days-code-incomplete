# ---------------------------------FUNCTION -------------------------------------
# def greet():
#     print("hello ")
#     print("how are you ")
# greet()
# ------------------------------------------------------------------------------
# def greet_name(name):
#     print(f"hello {name}")
#     print(f"where do you live {name}")
# greet_name("ashish")
# ----------------------------------------------------------------------------
# def greet(name,location):
#     print(f"hello {name}")
#     print(f"where is it like {location}")
# greet("ashish","bihar")
# -------------------------------------------------------------------------------
# coverage=5
# def paint_cal():
#     a=int(input("enter height "))
#     b=int(input("enter the width of the wall"))
#     cans=(a*b)/coverage
#     final=round(cans)  #or we can use math.ceil(cans)
#     print(final)
# paint_cal()
# ---------------------------------------------------------------------------------
def prime():
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("it is prime number ")
    else:
        print("it is not a prime number ")
number=int(input("enter the number to check : "))
prime()