#accept data from user and store it in the list
#till user enters end

plist=[]
p=input("Enter Product: ")
while p!="end":
    plist.append(p)
    p=input("Enter Product: ")

qlist=[]
q=int(input("Enter Quantity: "))
while q>=0:
    qlist.append(q)
    q=int(input("Enter Quantity: "))

for p,q in zip(plist,qlist):
    print(p,"-->",q)

#display only product with quantity > 50 and also show total quantity at end

tqty = 0
for p,q in zip(plist,qlist):
    if q>50:
        tqty = tqty + q
        print(p,"-->",q)
        
print("-"*60)
print("Total: ",tqty)
