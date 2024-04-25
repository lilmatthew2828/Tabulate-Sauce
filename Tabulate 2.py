# Matthew Kilpatrick
from tabulate import tabulate
def table():
    fileOfWeedStrains = open("WeedStrain.txt", 'w')
    ListOfStrains = [["Index", "Strains", "Indica, Sativa, or Hybrid"], [1, "Blue Dream", "Hybrid"],
                     [2, "Pineapple Express", "Hybrid"],
                     [3, "Sour Tangie", "Sativa"], [4, "Kushberry", "Indica"], [5, "Biscotti", "Hybrid"],
                     [6, "Lavender", "Indica"], [7, "Alaskan Thunder Fuck", "Hybrid"], [8, "Bruce Banner", "Hybrid"],
                     [9, "Jack Herer", "Sativa"],[10, "Grape Ape", "Indica"], [11, "Durban Poison", "Sativa"]]
    print(tabulate(ListOfStrains, headers="firstrow", tablefmt="pretty"))



class Employee:
    """Employee Class containing name, ssn and salary"""

    def __init__(self, name, ssn, salary):
        self.name = name
        self.ssn = ssn  ## Protected
        self.salary = salary  ## Private

Tom = Employee("Jack", 2222, 50000)

Jack = Employee("Jack", 2222, 50000)

print(Tom == Jack)


def __eq__(self, other):
    if (self.name == other.name):
        return True
    else:
        return False