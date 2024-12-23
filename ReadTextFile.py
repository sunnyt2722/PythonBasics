file = open('test.txt')
file2 = open('test.txt')

print(file.read(3))
print(file.readline())

line = file2.readlines()
for obj in line:
    print(obj)

file.close()