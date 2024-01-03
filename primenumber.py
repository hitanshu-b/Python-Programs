def checkPrime(n):5 
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num1 = int(input("Enter Number: "))
print(checkPrime(num1))

