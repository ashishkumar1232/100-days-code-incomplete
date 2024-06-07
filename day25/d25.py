# # CSV:- IT is very useful to show the data in tabular format . it stand for comma seperated values 
# # with open("weather_data.csv") as data_file:
# #     data=data_file.readlines()
# #     print(data)
# # ------------------------------------------------------------------------------
# # import csv
# # with open('weather.csv') as data_file:
# #     data=csv.reader(data_file)
# #     print(data)
# # ------------------------------------------------------------------------------
# # import csv
# # with open('/home/ashish/Documents/100DAYSCODES/day25/weather_data.csv') as f:
# #     data=csv.reader(f)
# #     tempratures=[]
# #     for row in data:
# #         if row[1] !="temp":
# #             tempratures.append(int(row[1]))
# #     print(tempratures)
# # ################################################################################
# #without using the pandas library there is big lines of code to view the csv file 
# # but using pandas library it has made simple 
# import pandas
# data=pandas.read_csv('/home/ashish/Documents/100DAYSCODES/day25/weather_data.csv')
# # print(data["condition"])
# # data_dict=data.to_dict() #this is to convert the gien data into ditionary
# # print(data_dict)
# # temp_list=data["temp"].to_list()
# # # average=sum(temp_list)/len(temp_list)
# # # print(average)
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # print(temp_list)
# # ------------------------------------------------------------------------------
# # #  get the data in column 
# # print(data["condition"])
# # print(data.condition)
# # ------------------------------------------------------------------------------
# #  get data in row 
# # print(data[data.day =="Tuesday"])
# # print(data[data.temp==data.temp.max()])
# # mon=data[data.day=="Monday"]
# # print(mon.condition)

# # =======\=========================\===================\=====================\===
# # CREATE THE DATAFRAME FROM SCRATCH
# data_dict={
#     "students":["ashish","ashok","yuvi","john"],
#     "marks":[80,67,89,65]
# }
# data=pandas.DataFrame(data_dict)#at first it will make the csv file and then we can use the file. dataframe is the keyword that is used to create the file
# data.to_csv("new_data.csv")
# print(data["students"])

import pandas 
data=pandas.read_csv('/home/ashish/Documents/100DAYSCODES/day25/sqirrel_count.csv')
grey_sq_count=len(data[data["Primary Fur Color"]=="Gray"])
red_sq_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_sq_count=len(data[data["Primary Fur Color"]=="Black"])
print(grey_sq_count)
print(red_sq_count)
print(black_sq_count)
dict_data={
    "Fur color":["Gray","Cinnamon","Black"],
    "count":[grey_sq_count,red_sq_count,black_sq_count]
}
# print(dict_data)
df=pandas.DataFrame(dict_data)
df.to_csv("new_squirell_count.csv")












