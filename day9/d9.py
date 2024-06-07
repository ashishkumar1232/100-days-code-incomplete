# -----------------------DICTIONARIES---------------------------------------------
# it can be written as {key : value}
dictionary={
    "bug":"something answer",
    "loop":"something",
    "function":"the answer"
}
dictionary["bug"]="something another answer to overwrite" #it is to change the dictionary
# print(dictionary["bug"])
for key in dictionary:
    print(key)
    # print(dictionary[key])
    
# --------------------------------------------------------------------------------
# studentscore={
#     "ashish":97,
#     "yuvraj":89,
#     "punit":90,
#     "shubham":68,
#     "abhijeet":99,
# }
# studentgrade={}
# for i in studentscore:
#     student=studentscore[i]
#     if student >90:
#         studentgrade[i]="outstanding"
#     elif student >80:
#         studentgrade[i]="expected expaction"
#     elif student >70:
#         studentgrade[i]="excellent"
#     elif student >60:
#         studentgrade[i]="nice job"
# print(studentgrade)
# ------------------------------------------------------------------------------
# -------------------NESTING A DICTIONARY WITH A LIST AND DICTIONARY-----------
# travel={
#     "france":{"country_visited":["nepal","bhutan","china"]},
#     "uk":["germany","belgium"]
# }
# print(travel["uk"])
# pythontutor.com is website for line by line code checking