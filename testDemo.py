class Calculator:
    num=150

    # This is the constructor! gets called as soon as an object is created. Here the a and b are instance variables
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    def addNum(self):
        return self.a + self.b + Calculator.num

obj = Calculator(15,20)
# print(obj.addNum())