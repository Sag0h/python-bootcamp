# with open(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\pandas-practice\weather_data.csv", mode="r")as file:
#     data = file.readlines()
# print(data)

# import csv

# with open(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\pandas-practice\weather_data.csv")as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)

import pandas as pd

# data = pd.read_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\pandas-practice\weather_data.csv")
# print(data)

# data_dict = data.to_dict()

# data_temp_list = data["temp"].to_list()

# print(sum(data_temp_list) / len(data_temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# # print(9.0/5.0 * (int(monday.temp)) + 32)

# # Create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores":[76, 56, 65]   
# }

# data = pd.DataFrame(data_dict)
# data.to_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\pandas-practice\new_data.csv")

squirrel_data = pd.read_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\pandas-practice\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["grey", "red", "black"]
dict = {"Fur Color": colors,
}

dict["Counts"] = squirrel_data["Primary Fur Color"].value_counts().to_list()


pd.DataFrame(dict).to_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\pandas-practice\squirrel_count.csv")
