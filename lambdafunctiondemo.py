lst=[12,14,1,4,5]
lst1=[]
for num in lst:
    if num%2==0:
        lst1.append(num)
print(lst1)

print("Using Lambda function")
lst1=list(filter(lambda x:x%2==0 and x>10 ,lst))
print(lst1)
