#enumerate

lst = [23,34,53,12,18]
i=0
for num in lst:
    print(i,"--->",num)
    i+=1

for index,num in enumerate(lst):
    print(index,"--->",num)

lst1 = ["Pune","mumbai","nashik","Nagpur"]
for index,num in enumerate(lst1,1):
    print(index,"--->",num)

lst1 = ["Pune","mumbai","nashik","Nagpur"]
for i in enumerate(lst1,10):
    print(i)
