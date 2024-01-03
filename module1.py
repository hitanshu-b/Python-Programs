def addition(a,b,*t):
    s=0
    s=a+b
    for n in t:
        s+=n
    return n

def printTable(n=5):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)

if __name__=="__main__":
    print("aaaa",__name__)
    printTable(3)
    printTable(4)
    addition(2,3)
    addition(2,3,4,5,6,7)
