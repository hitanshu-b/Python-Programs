class Person:
    def __init__(self, pid=0, pname="", mob=""):
        print("in person init")
        self.__pid = pid
        self.__pname = pname
        self.__mob = mob

    def __str__(self):
        print("in str")
        return "Pid: " + str(self.__pid) + "\nName: " + self.__pname + "\nMob: " + self.__mob

    # getter and setter
    def getPid(self):
        return self.__pid

    def getPname(self):
        return self.__pname

    def getMob(self):
        return self.__mob

    def setPid(self, pid):
        self.__pid = pid

    def setPname(self, pname):
        self.__pname = pname

    def setMob(self, mob):
        self.__mob = mob

class Employee(Person):
    def __init__(self, pid=0, pname="", mob="", dept="", desg=""):
        # Person.__init__(self,pid,pname,mob)
        super().__init__(pid,pname,mob)
        print("in employee init")
        self.__dept = dept
        self.__desg = desg

    def __str__(self):
        return "\nDepartment: " + self.__dept + "\nDesignation: " + self.__desg
    def setDept(self,dt):
        self.__dept = dt
    def setDesg(self,ds):
        self.__desg = ds
    def getDesg(self):
        return self.__desg
    def getDept(self):
        return self.__dept

class SalariedEmp(Employee):
    def __init__(self, pid=0, pname="", mob="", dept="", desg="", sal=0):
        super().__init__(pid, pname, mob, dept, desg)
        self.__sal = sal

    def __str__(self):
        return super().__str__()+"\nSalary: "+str(self.__sal)
    def getSal(self):
        return self.__sal
    def setSal(self,s):
        self.__sal = s

if __name__ == "__main__":
    s1 = SalariedEmp(12, "rene","32432", "hr", "Manager",444444)
    print(s1)

#    e1 = Employee(12,"reane","32432", "hr", "Manager")
#   print(e1)
# p = Person(12, "asdaerd", "2123434")
# print(p)
