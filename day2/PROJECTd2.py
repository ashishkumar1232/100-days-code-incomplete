print("Welcome to the tip calculator")
bill=float(input("what was the total bill ?\n"))
per=int(input("what percentage tip would you like to give?10,12,15?\n"))
total=bill+((per/100)*bill)
person=int(input("how many people to split the bill ?\n"))
each=total/person
print("each person should pay ",round(each,2))