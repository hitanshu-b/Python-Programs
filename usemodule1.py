import sys
import module1 as m
#from module1 import addition,printTable
#from module1 import *

choice = 0
print("bbbb",__name__)
while choice != 3:
    print("1. Addition")
    print("2. PrintTable")
    choice=int(input("Enter Choice: "))
    if choice == 1:
        s1 = m.addition(2,3,4,5,6)
        print("Addition: ",s1)
    elif choice == 2:
        n=3
        m.printTable(3)
    else:
        sys.exit(0)
    

