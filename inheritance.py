from oop import Calculator

class ChildImplementation(Calculator):
    num2 = 300
    
    def __init__(self):
        Calculator.__init__(self, 2 ,9)
    
    def getCompleteData(self):
        return self.num2 + self.num + self.Sum()
    
obj = ChildImplementation()
print(obj.getCompleteData())