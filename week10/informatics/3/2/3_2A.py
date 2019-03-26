from math import sqrt

a = input()
a = int(a)
i = 1
while i < a+1:
    if int(float(sqrt(i)))*int(float(sqrt(i))) == int(i):
        print(i)
    i += 1
