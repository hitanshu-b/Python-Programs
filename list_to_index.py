lst=[15,3,4,5,7,8,6,8]
m = max(lst)
lst1=[]
for i in range(m+1):
    lst1.append(-1)
i=0
print(lst)
for num in lst:
    lst1[num]=i
    i=i+1
print(lst1)
