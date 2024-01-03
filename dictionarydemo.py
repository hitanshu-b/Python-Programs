courses={"DBDA":59,"DAC":200,"DITISS":50,"DMC":43}
print(courses)
print("DITISS",courses["DITISS"])
print("DITISS",courses["DBDA"])

num=int(input("Enter Number: "))
for k in courses.keys():
    if courses[k] > num:
        print(k,"--->",courses[k])
