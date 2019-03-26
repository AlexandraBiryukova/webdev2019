from math import sqrt

a = input()
a = int(a)
for i in range(2,a+1):
    if a%i==0:
        print(i)
        break