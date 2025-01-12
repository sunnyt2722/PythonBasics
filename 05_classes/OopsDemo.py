class Calculator:
    num=100

    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("Constructor called")

    def sum(self):
        return self.firstNumber + self.secondNumber

    def sub(self):
        return self.firstNumber - self.secondNumber

    def mul(self):
        return self.firstNumber * self.secondNumber

    def div(self):
        return self.firstNumber / self.secondNumber

object = Calculator(12,3)
print(object.num)
print(object.sum())
print(object.sub())
print(object.mul())
print(object.div())
print("I am called ")