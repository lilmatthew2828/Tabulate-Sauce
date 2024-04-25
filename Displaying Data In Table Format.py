# Matthew Kilpatrick
# 2-26-24
# Introduction to the tabulate import
from tabulate import tabulate         # ⟸⟸ import statement for tabulate functions
import random
# Example 1 :
# Creating a 2-dimensional list:
def main():
    # open a new file to write to:
    fileForTableData = open("TableData.txt", 'w')
    table_data = [['Name' , 'Age' , 'Job'],
                            ['Machew' , '21' , 'Programmer'],
                            ['Raven' , '21' , 'Architecture'],
                            ['LUCKI' , '35' , 'THE God Of  Literature'],
                            ['John' , '20' , 'Sports Manager'],
                            ['Ibn' , '22' , 'Rapper']]
    table_data2 = [["Sun",696000,1989100000],["Earth",6371,5973.6],
                              ["Moon",1737,73.5],["Mars",3390,641.85]]
    #print()
    fileForTableData.write("Table 2 With Header: ")
    fileForTableData.write("\n")
    # Headers: The second optional argument named "headers:" defines a list of column headers to be used
   # print(tabulate(table_data2, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))
    fileForTableData.write(tabulate(table_data2, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))
    fileForTableData.write("\n")
    # Using the imported tabulate function to print the table:
    # IF HEADERS = "firstrow", the the first row of data is used to be the header:
   # print("Using The Tabulate Function To Print Table 1: ")
    fileForTableData.write("\n")
    fileForTableData.write("Using The Tabulate Function To Print Table 1: ")
    fileForTableData.write("\n")
    #print(tabulate(table_data, headers ="firstrow", tablefmt="psql"))
    fileForTableData.write(tabulate(table_data, headers ="firstrow", tablefmt="psql"))
    #print(tabulate([["Name", "Age"], ["Alice", 24], ["Bob", 19]],  headers = "firstrow"))
    ListOfStrains = [["Strains", "Indica, Sativa, or Hybrid"], ["Blue Dream", "Hybrid"], ["Pineapple Express", "Hybrid"],
                                ["Sour Tangie", "Sativa"], ["Kushberry", "Indica"], ["Biscotti", "Hybrid"],
                                ["Lavender", "Indica"], ["Alaskan Thunder Fuck", "Hybrid"], ["Bruce Banner", "Hybrid"],
                                ["Jack Herer", "Sativa"]]
    #print(tabulate(ListOfStrains, headers="firstrow"))
   # print()
    fileForTableData.write("\n")
    fileForTableData.write("\n")
    fileForTableData.write(tabulate(ListOfStrains, headers="firstrow"))
    fileForTableData.write("\n")
    fileForTableData.write("\n")
    fileForTableData.write("Psql:\n")
    fileForTableData.write(tabulate(table_data, headers="firstrow", tablefmt='psql'))
    fileForTableData.write("\n")
    fileForTableData.write("\n")
    fileForTableData.write("Pretty: \n")
    fileForTableData.write(tabulate(ListOfStrains, headers='firstrow', tablefmt='pretty'))
    fileForTableData.write("\n")
    fileForTableData.write("\n")
    fileForTableData.write("Fancy Grid: \n")
    fileForTableData.write(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
    fileForTableData.write("\n")
    fileForTableData.write("\n")
    fileForTableData.write("Heavy Outline: \n")
    fileForTableData.write(tabulate(ListOfStrains, headers="firstrow", tablefmt="heavy_outline"))
    # Table Format Functions:
    print()
    print("Regular Print, No Read:")
    print(tabulate(ListOfStrains, headers="firstrow", tablefmt='psql'))
    # Close the file:
    fileForTableData.close()
if __name__ == '__main__':
    main()
print()  #Space
# Reading From the file:
print("Reading From The File: ")
def RavenMills():
    readFromFile = open("TableData.txt", 'r')
    for lines in readFromFile:
        tables = str(lines)
        print(tables, end="")
    readFromFile.close()
if __name__ == '__main__':
    RavenMills()

# Using a nested for-loop
#print('Basic Nested For-Loop Print:  ')
#for row in table_data:
   # for col in row:
      #  print(f'{col}', end= " ")
    #print()
#print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#data = [['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5], ['six', 6], ['seven', 7], ['eight', 8], ['nine', 9], ['ten', 10]]
#index = int(0)

# This gets the longest string so we can print every row without having to change the variables
#longest = 0
#for row in data:
   # length = len(row[0])
    #f(length > longest):
    #    longest = length

#for row in data:
   # spaces = (longest-len(row[0])) * " "
    #print(row[0],spaces , row[1])
#print("Example 2 with Tabulate Package: ")
#print(tabulate(data))

def MachewXCody():
    file = open("ArtistFile.txt", 'w')
    table_of_nums = [[], [], [], [], [], [],[]]

