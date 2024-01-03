import sys
def addNewCourse(courses,cName,num):
    v=courses.get(cName,-1)
    if v==-1:
        courses[cName]=num
        return 1
    else:
        ans=input("Duplicate Key Overwrite?")
        if ans == "y":
            courses[cName]=num
            return 2
        else:
            return 3

def displayAll(courses):
    for k, v in courses.items():
        print(k,"---->",v)

def deleteCourse(courses,cName):
    v= courses.get(cName,-1)
    if v!=-1:
        return True
    else:
        return False

def updateCourse(courses,cName,num):
    v=courses.get[cName,-1]
    if v==-1:
        return False
    else:
        courses[cName]=num
        return True

def displayByNum(courses,num):
    for k in courses.keys():
        if course[k]>num:
            print(k,"---->",courses[k])
    return True

courses={}
choice=0
while choice!=6:
    print("1. Add New Course\n2. Delete the Course\n3. Display All Courses")
    print("4. Display Details of Courses with No. of Students > given Value")
    print("5. Update Course\n6. Exit")

    choice = int(input("Enter Your Choice: "))
    if choice==1:
        cName=input("Enter CourseName: ")
        num=int(input("Enter Number: "))
        status=addNewCourse(courses,cName,num)
        if status==1:
            print("Key Added")
        elif status==2:
            print("Key Overwritten")
        else:
            print("Duplicate Key")

    elif choice==2:
        cName=input("Enter CourseName: ")
        status=deleteCourse(courses,cName)
        if status:
            print("Course Deleted")
        else:
            print("Course Not found")

    elif choice==3:
        displayAll(courses)
        
    elif choice==4:
        displayByNum(courses,num)

    elif choice==5:
        cName=input("Enter CourseName: ")
        num=int(input("Enter Num: "))
        status=updateCourse(courses,cName,num)
        if status:
            print("Course Updated")
        else:
            print("Course Not Found")

    elif choice==6:
        sys.exit(0)
    
