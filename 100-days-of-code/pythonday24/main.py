# with open("weather_data.csv.csv") as data_file:
#      data=data_file.readlines()
#      print(data)
#
# import csv
#
# with open("weather_data.csv.csv") as data_file:
#      data=csv.reader(data_file)
#      temperatures=[]
#      for row in data:
#           if row[1] != "temp":
#                temperatures.append(int(row[1]))
# #      print(temperatures)
#
# import pandas
#
# data=pandas.read_csv("weather_data.csv.csv")
# print(data["temp"])

import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv.csv")
grey_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])


print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict={
    "Fur color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrel_count,red_squirrel_count,black_squirrel_count]

}
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")