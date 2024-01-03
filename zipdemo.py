#zip
#enumerate
#sorted
#reversed

batch = ["DBDA","DAC","DITISS","DMC"]
participants = [45,200,60,56]

i=0
for i in range(len(batch)):
    print(batch[i],"---->",participants[i])
    i+=1

for i,j in zip(batch,participants):
    print(i,"---->",j)
