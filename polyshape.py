from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self, color="White"):
        self.__color = color
    def __str__(self):
        return "Color: "+self.__color
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def getColor(self):
        return self.__color

class Triangle(Shape):
    def __init__(self, color="White", b=0, h=0, s1=0, s2=0):
        super().__init__(color)
        self.__b = b
        self.__h = h
        self.__s1 = s1
        self.__s2 = s2
    def __str__(self):
        return super().__str__()+"B: "+str(self.__b)+"H: "+str(self.__h)+"S1: "+str(self.__s1)+"S2: "+str(self.__s2)
    def area(self):
        return 0.5 * self.__b * self.__h
    def perimeter(self):
        return self.__b + self.__s1 + self.__s2

class Circle(Shape):
    def __init__(self, color="White", r=0):
        super().__init__(color)
        self.__r = r
    def __str__(self):
        return super().__str__()+"R: "+str(self.__R)
    def area(self):
        return 3.142 * self.__r * self.__r
    def perimeter(self):
        return 2 * 3.142 * self.__r
