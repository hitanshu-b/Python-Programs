#Delete employee from file

def readData():
    with open("empdata.dat") as fh:
        lst=fh.readlines()
        return lst

def deleteEmp(lst,eid):
    for i,emp in enumerate(lst):
        elist=emp.split(":")
        if int(elist[0])==eid:
            #lst.remove(emp)
            lst.pop(i)
            return True
    return False

def writeData(lst):
    with open("empdata.dat","w") as fh:
        for emp in lst:
            fh.write(emp)


lst=readData()
print(lst)
eid=int(input("Enter Eid: "))
flag=deleteEmp(lst,eid)
if flag:
    print("deleted")
else:
    print("Not found")
print(lst)
writeData(lst)
