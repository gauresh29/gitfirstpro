from  abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(Shape):
    type=4
    side=3
    def __init__(self):
        self.length=4
        self.width=3
    def printarea(self):
        return self.length*self.width


rect1=rectangle()
print(rect1)