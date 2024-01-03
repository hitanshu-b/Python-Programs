from polyshape import *
import sys
lst = []
choice = 0
while choice !=4:
    print("1. Triangle\n2. Circle\n3. Rectangle\n4.Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        s = Triangle("Red",5,6,3,2)
    #    print("Area: ",s.area())
    #    print("Perimeter: ",s.perimeter())
    elif choice == 2:
        s = Circle("Yellow",5)
    #    print("Area: ",s.area())
    #    print("Perimeter: ",s.perimeter())
    else:
        break
    lst.append(s)

ctr = 0
ctc = 0
for ob in lst:
    print("Area: ",ob.area())
    print("Perimeter: ",ob.perimeter())
    if isinstance(ob,Triangle):
        ctr = ctr+1
        if ob.getColor() == "red":
            print("Rectange is red")
    elif isinstance(ob, Circle):
        ctc = ctc + 1
print(ctr)
print(ctc)
