from OopsDemo import Calculator

class ChildClass(Calculator):

    def ChildClass(__self__,a,b):
        Calculator.__init__(__self__,a,b)
        print("This is child class constructor")

    def PrintName(self,name):
        print("Name Printed is ",name)

childObject = ChildClass(10,4)
childObject.PrintName("Sunny")
