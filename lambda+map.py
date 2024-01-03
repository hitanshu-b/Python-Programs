def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

lst=[4,6,3]

lst3=list(map(lambda a:factorial(a),lst))
print(lst3)
