class Person:
    def __init__(self,pid=0,pname="",mob=""):
        print("In person init")
        self.__pid=pid
        self.__pname=pname
        self.__mob=mob
        self._data=100
    def __str__(self):
        print("in str")
        return "Pid: "+str(self.__pid)+"\nName: "+self.__pname+"\nMob: "+self.__mob
    def getPid(self):
        return self.__pid
    def getPname(self):
        return self.__pname
    def getmob(self):
        return self.__mob
    def setPid(self,pid):
        self.__pid=pid
    def setPname(self,nm):
        self.__pname=nm
    def setMob(self,m):
        self.__mob=m
        

p=Person(12,"jdsjfsdhfk","7887977")
print(p)
print(p._data)
p1=Person(12,"afjkdk","6f76s7f")
print(p1)
