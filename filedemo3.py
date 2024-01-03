lst=[]
with open("empdata.dat") as fh:
    for line in fh:
        lst.append(line)

with open("empdata.dat") as fh:
    lst=fh.readlines()
print(lst)
