# Input always returns String
name = input("Enter your name : ")
print(name)

length = int(input("enter length of property : "))
breadth = int(input("enter breadth of property : "))
area = length * breadth
print(f"Area is {area}")
print("Area is {}".format(area))