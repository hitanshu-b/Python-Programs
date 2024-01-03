def myFunction(a=2,b=5,c=4,d=5):
    print("a:",a,"b:",b,"c:",c,"d:",d)
    print(a,a+10)
    print(b,b+20)
    return c+20,d-5

def addition(a,b,*t):
    print(a,b)
    print(t)
    s=0
    s=a+b
    for num in t:
        s=s+num
    return s

def function1(a,b,**p):
    print(a,b)
    print(p)

def function2(a,b,*t,**p):
    print(a,b)
    print(p)
    print(t)

function2(12,11,23,4,5,6,"sdfd","waee",x=23,y=43)

    
function1(12,13,x=344,y=45,z=67)
    
a=addition(12,10)
print(a)
b=addition(1,2,3,4,5,6,7,8,9,10)
print(b)

print(myFunction(12,13,23,15))
print(myFunction(12))
print(myFunction(12,34))
