#  classes are user defined blueprint or prototype
# ex: calculatr - sum, multiply, subtraction


# self keyowwrd is mandatory for calling variable names into methods
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 300
    
    # default constructor 
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        
        print("I am called automatically when the object is created")
    
    def getData(self):
        print("I am not executing the method in the class")
        
    def Sum(self):
        return self.firstNumber + self.secondNumber + Calculator.num 
        
obj = Calculator(2, 3)
obj.getData()
print(obj.Sum())