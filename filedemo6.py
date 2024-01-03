def readData():
    with open("empdetails.dat") as fh:
        lst=fh.readlines()
    return lst

def acceptData(lst):
    empid= input("Enter EmpID: ")
    ename = input("Enter Name: ")
    sal = input("Enter Salary: ")
    desg = input("Enter Desg: ")
    s1=empid+":"+ename+":"+sal+":"+desg+"\n"
    lst.append(s1)

def appendData(lst):
    with open("empdetails.dat","a") as fh:
        for emp in lst[cnt:]:
            print(emp)
            fh.write(emp)

def updateData(lst):
    for i,emp in enumerate(lst):
        empdata=emp.split(":")
        if empdata[-1].rstrip("\n")=="Manager":
            empdata[-2]=str(int(empdata[-2])+1000)
        elif empdata[-1].rstrip("\n")=="Analyst" or empdata[-1].rstrip("\n")=="Engineer"
            empdata[-2]=str(int(empdata[-2])+800)
        elif empdata[-1].rstrip("\n")=="Designer":
            empdata[-2]=str(int(empdata[-2])+800)
        elif empdata[-1].rstrip("\n")=="Programmer":
            empdata[-2]=str(int(empdata[-2])+700)

            s1=":".join(empdata)
            print(lst)
            lst[i]=s1
            print(lst)

def overWrite(lst):
    with open("empdetails.dat","w") as fh:
        for emp in lst:
            print(emp)
            fh.write(emp)

print("1. Add Employee\n2. Update Employee\n3. Exit")
choice=int(input("Enter Choice: "))
lst=readData()
cnt=len(lst)
print(cnt)
if choice==1:
    ans="y"
    while ans=="y":
        acceptData(lst)
        ans=input("Continue")
        print(lst)
    appendData(lst)
elif choice == 2:
    updateData(lst)
    overWrite(lst)
