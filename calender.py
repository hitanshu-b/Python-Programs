days = int(input("Enter Days: "))
start = int(input("Start of the month: "))
print(" "*6*start)
print("Mo\tTu\tWe\tTh\tFr\tSa\tSu")
print("\t"*start,end=" ")
count=start
for i in range(1,days+1):
    print(i,end="\t")
    count=count+1
    if count==7:
        print()
        count=0
