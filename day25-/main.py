# with open(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-\weather_data.csv", mode="r")as file:
#     data = file.readlines()
# print(data)

# import csv

# with open(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-\weather_data.csv")as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)

import pandas as pd

pd.read_csv()