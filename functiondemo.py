def printtable(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def increament(x,y):
    x+=10
    y+=20
    return x,y

num = int(input("Enter Number: "))
printtable(num)

num = int(input("Enter Number: "))
f = factorial(num)
print("Factorial: ",f)

a = int(input("Enter Num1: "))
b = int(input("Enter Num2: "))
a,b = increament(a,b)
print(a,b)
