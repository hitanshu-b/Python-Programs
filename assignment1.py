lst = []
n=1
while(True):
    num1 = int(input("Enter Number: "))
    if num1%7!=0:
        lst.append(num1)
    else:
        break
print(lst)

l = []
x= int(input("Enter the Number: "))
while x%7!=0:
    l.append(x)
    x=int(input("Enter the number: "))
print(l)
