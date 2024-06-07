from replit import clear 
from art import logo
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    print(logo)
    num1=float(input("enter the first number ? :"))
    for symbol in operation:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("enter the operation : ")
        num2=float(input("enter the second number ? : "))
        calculation_function=operation[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"enter y to continue with {answer} and n to start new calculation : ")=='y':
            num1=answer
        else:
            should_continue=False
            clear()
            calculator()
calculator()