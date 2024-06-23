from testDemo import Calculator


class ChildCalc(Calculator):


    num3=500

    
    # When inherting from parent class we need to first call the constructor
    # if the parent class has a constructor
    # defined by the user(not required if it is a default constructor)
    def __init__(self, a, b):
        Calculator.__init__(self, a, b)

    def summation(self):
        return self.num3 + self.num + self.addNum()

obj = ChildCalc(1000, 1)
print(obj.summation())
