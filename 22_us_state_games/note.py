# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row == ['day', 'temp', 'condition']:
#             pass
#         else:
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# summ = 0
# for num in temp_list:
#     summ += num
# avg = summ / len(temp_list)

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp += 33.8
# print(monday_temp)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
grey = 0
red = 0
black = 0
for color in fur_color:
    if color == "Gray":
        grey += 1
    elif color == "Cinnamon":
        red += 1
    elif color == "Black":
        black += 1
    else:
        pass
print(grey)
print(red)
print(black)

