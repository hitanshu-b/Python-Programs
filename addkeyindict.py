courses={"DBDA":59,"DAC":200,"DITISS":50,"DMC":43}
cname=input("Enter Course Name: ")
num=int(input("Enter Number: "))
v=courses.get(cname,-1)
if v==-1:
    courses[cname]=num
else:
    ans=input("Duplicate Key Overwrite")
    if ans=="y":
        courses[cname]=num
    else:
        print("Duplicate Key")
print(courses)

del(courses["DAC"])
print(courses)
