from math import sqrt

a = input()
b = input()
a = int(a)
b = int(b)
for i in range(a,b+1):
    if int(float(sqrt(i)))*int(float(sqrt(i))) == int(i):
        print(i)