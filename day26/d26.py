# #LIST COMPREHENSION :-
# #suppose the example while we add 1 to every element of the list 
# l=[1,2,3,4,5]
# # nl=[]
# # for i in l:
# #     addn=i+1
# #     nl.append(addn)
# # print(nl)
# #BUT USING THIS IS NOT GOOD AS IT IS LONG SO WE CAN COMPREHENSION  WHICH IS SHORTER AND MORE EFFICIENT.
# nl=[n+1 for n in l]
# print(nl)
# # THE LIST COMREHENSION IS LOOOKING LIKE THIS :
# # new_list=[new_item for item in list]-----------this is the  general form of list comprehension
# new_l="Ashish"
# new_nl=[n for n in new_l]
# print(new_nl)
# # ---------------------------------------------------------------------------
# num=[1,2,3,5,8,7]
# new_num=[i*2 for i in range(1,5)]
# print(new_num)
# # -------------------------------------------------------------------------------
# # HOW TO USE IF SATATEMENT IN LIST COMPREHENSION 
# #-------- new_list=[new_item for item in list if test]-------------------IT IS THE GENERAL FORM OF IF LIST COMPREHENSION

# names=["ashish","yuvraj","abhijeet","akash",'anand',"sachin",'rahul',"dravid"]
# new_names=[n for n in names if len(n)<6]
# print(new_names)
# --------------------ALL THE LIST IN CAPS -------------------------------------------------------------
# namea=["ashish","yuvraj","abhijeet","akash",'anand',"sachin",'rahul',"dravid"]
# new_namea=[n.upper() for n in namea]
# print(new_namea)
# ----------------------SQUARE OF THE LIST ------------------------------------------------------------
# # list=[0,1,2,3,4,5,6,7,8,9]
# squared_list=[i**2 for i in range(0,10) ]
# print(squared_list)
# --------------------EVEN  NUMBERS FROM A LIST-------------------------------------------------------  
# lis=input("Enter a number").split(",")
# list=[int(i) for i in lis ]
# print(list)
# -----------------------------------------------------------------------------
# ============================DICTIONARY COMPREHENSION ========================
# -----------------------------------------------------------------------------
# new_dict={new_key:new_value for item in list}##this is the general form of dictionary comprehension.
# import random
# names=["ashish","yuvraj","abhijeet","akash",'anand',"sachin",'rahul',"dravid"]
# new_dict={student:random.randint(0,100) for student in names}
# print(new_dict)
# # passed_student={new_key:new_value for (key,value)in dictionary.items()}----IT IS THE GENERAL FORM 
# passed_student={student:score for (student,score)in new_dict.items() if score>=60}
# print(passed_student)
# -----------------------------------------------------------------------------
# sentences=input()
# result={word:len(word) for word in sentences.split()}
# print(result)
# ----------------------------------------------------------------------------
# eval converts correctly formatted string to dict 
weather_c=eval(input())
weather_f={day:temp*9/5+32 for (day,temp) in weather_c.items()}
print(weather_f)
