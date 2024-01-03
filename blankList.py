lst=[]
num=0
while num!=-1:
    num=int(input("Enter Number: "))
    d=num%10
    while len(lst)<=d:
        lst.append([])
    lst[d].append(num)
    print(lst)
