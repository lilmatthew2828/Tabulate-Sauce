import inline
import pandas
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import flet
import numpy
import random
import pygame
import pprint
from flet import TextField, Checkbox, ElevatedButton, Text,Row, Column
from flet_core.control_event import ControlEvent
import sqlite3
# print("Hi! This is a cell. Press the ▶ button above to run it")
# def print_10_nums():
#     for i in range(10):
#         print(i, end=',')
# time = sum([x for x in range(100000)])
# print(time)
#
#
# # 1.1 Reading data from a csv file
# plt.style.use('ggplot')  #Make the graphs a bit prettier, and bigger
# plt.rcParams['figure.figsize'] = (15,5) # Make the graphs a bit prettier, and bigger
# '''
# You can read data from a CSV file using the read_csv function. By default, it assumes that the fields are comma-separated.
# '''
# broken_dataframe = pd.read_csv('/Users/machew/PycharmProjects/firstpythoncode/pythonProject/pandas-cookbook-master/data/bikes.csv',encoding='ISO-8859-1')
# print("Printing The First 3 rows from the broken dataframe: ")
# # print(broken_dataframe)
# print(broken_dataframe[:3]) # first 3 rows
# print()
# print()
# numOfRowsToPrint = int(3)
# numOfRowsToPrint2 = int(5)
# count = int(1)
# indexs = []
# indexs2 = []
# count2 = int(1)
# smallerBrokenDataFrame = broken_dataframe[:5] # making a smaller broken dataframe of the already broken dataframe
# print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# print(f"This is the SMALLER BROKEN DATAFRAME:\n{smallerBrokenDataFrame}") #
# for x,y in smallerBrokenDataFrame.items():
#     for d in y:
#         indexs2.append(count2)
#         count2 += 1
# print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# print(f"These are going to be the indexes for the Smaller Broken DataFrame: {indexs2}\n"
#       f"Printing The Smaller Broken DataFrame With The Tabulate Package: ")
# print(tabulate(smallerBrokenDataFrame,headers=['ID',f"First {numOfRowsToPrint2} Rows Of The .CSV File"], tablefmt='heavy_outline',numalign='middle',showindex=indexs2))
#
# print("\t✮ You'll notice that this is totally broken! read_csv has a bunch of options that will let us fix that, though.")
# print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# # Below is what I will be doing to fix the original broken dataframe
# '''
#     1. change the column separator to a ;
#     2. Set the encoding to 'latin1' (the default is 'utf8')
#     3. Parse the dates in the 'Date' column
#     4. Tell it that our dates have the day first instead of the month first
#     5. Set the index to be the 'Date' column
# '''
# kp = int(1)
# l = []
# fixed_dataFrame = pd.read_csv('/Users/machew/PycharmProjects/firstpythoncode/pythonProject/pandas-cookbook-master/data/bikes.csv',sep=";",encoding='latin1',parse_dates=['Date'],dayfirst=True,index_col='Date')
# for x,y in fixed_dataFrame.items():
#     for data in y:
#         l.append(kp)
#         kp += 1
# print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# print("Printing The First 8 Rows Of The Fixed DataFrame Using Tabulate: ")
# print(tabulate(fixed_dataFrame[:8],tablefmt='heavy_outline',headers=fixed_dataFrame.columns))
# print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# print(f"Printing The First 8 Rows Of The Fixed DataFrame Using Regular Print and The to_string method to print all the columns:\n"
#       f"{fixed_dataFrame[:8].to_string()} ")
# print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# line = "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
# # Selecting A Particular Column: When you read a CSV, you get a kind of object called a DataFrame, which is made up of rows and columns.
# # You get columns out of a DataFrame the same way you get elements out of a dictionary.
# print("Examples Of Selecting Individual Rows From A DataFrame: ")
# print(fixed_dataFrame['Berri 1'])
# fixed_dataFrame['Berri 1'].plot()
# plt.show()
# fixed_dataFrame.plot(figsize=(17, 10))
# plt.show()
# 9.1 Reading Data From Sql Databases:
index = int(1)
con = sqlite3.connect('/Users/machew/PycharmProjects/firstpythoncode/pythonProject/pandas-cookbook-master/sqlite (2).db')
print()
print(f"{index}. Reading From The Sales Person Table:")
range1 = int(5)
dataframe = pandas.read_sql(f'SELECT * from Salesperson  LIMIT 5', con) # <----- Turning It into a dataframe to print
c = int(1)
raven = []
for nums in range(range1): # <===== Making a list to store number up to however many rows are in the dataframe
    raven.append(nums+1)
print(f"\t# Of Items/Rows In This DataFrame To show that It only limit to 5 rows: count = {len(raven)}")
print(f"\tThis is the list of indexs that will be printed within the table: {raven}")
print(tabulate(dataframe,headers=dataframe.columns,showindex=raven,tablefmt='pretty'))
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
dataframe2 = pandas.read_sql('SELECT * from Vehicles LIMIT 4', con) # <----- Turing it into a dataframe to print
# Getting the list of index:
count = int(1)
l = []
for x in range(4):
    l.append(x + 1)
print(f"{index+1}. Reading From The Vehicle` Table:")
print(f"\t# Of Items/Rows In This DataFrame To show that It only limits to 4 rows: count = {len(l)}")
print(f"\tThis is the list of numbers up to 4 that we will be using as our index: {l}")
print(tabulate(dataframe2,headers=dataframe2.columns,showindex=l,tablefmt='fancy_outline'))
print("\n--------------------------------------------------------------------------------------------------------------------------------------------\n")
dataframe3 = pandas.read_sql('SELECT * from Vehicles LIMIT 3', con) # <----- Turing it into a dataframe to print
# Getting the list of index:

l = []
for x in range(3):
    l.append(x + 1)
print(f"{index+2}. Reading From The Vehicle` Table:")
print(f"\t# Of Items/Rows In This DataFrame To show that It only limits to 4 rows: count = {len(l)}")
print(f"\tThis is the list of numbers up to 3 that we will be using as our index: {l}")
print(tabulate(dataframe3,headers=dataframe3.columns,showindex=l,tablefmt='fancy_outline'))






#
#
#
#
# # Getting the index:
# ind = int(1)
# poke = []
#
# print("This is the pokemon.csv file but the first 10 rows: ")
# pokemon_work = pd.read_csv("/Users/machew/PycharmProjects/firstpythoncode/pythonProject/Pokemon/pokemon_data.csv")
# police_shootings_work = pd.read_csv("/Users/machew/PycharmProjects/firstpythoncode/pythonProject/Project 2 - Data Science - Fatal Police Shootings/fatal-police-shootings-data.csv")
# print(pokemon_work[:10])
# df = pokemon_work[:10]
# for x in df.iterrows():
#     for d in x:
#         poke.append(ind)
#         ind+=1
# print(poke)
# # for x,y in first10ofpoke.items():
# #     for r in x:
# #         poke.append(ind)
# #         ind+=1
# # print(poke)
# # print(first10ofpoke)
#
# print(tabulate(pokemon_work[:20],tablefmt="double_outline",showindex=poke,headers=pokemon_work.columns))
#
#
#
# def popup(page: flet.Page): # Making the page itself
#     page.title = "Pokemon.CSV"
#     page.window_height = 1500
#     page.window_width = 1500
#     title = flet.Text(value="Pokemon.csv", color="orange")
#     page.controls.append(title)
#     page.add(flet.SafeArea(flet.Text(f"{tabulate(pokemon_work[:20],tablefmt='heavy_outline',showindex=poke,headers=pokemon_work.columns)}\n\n")))
#     end_title = flet.Text(value="--------------End Of File Here--------------",color='orange')
#     page.controls.append(end_title)
#     #page.add(flet.SafeArea(flet.Text(tabulate(police_shootings_work[:20],tablefmt="double_outline",showindex=poke,headers=pokemon_work.columns))))
#     # page.add(flet.SafeArea(flet.Text(pprint.pprint(police_shootings_work))))
# flet.app(popup)



