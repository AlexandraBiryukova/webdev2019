from math import sqrt

a = input()
a = int(a)
for i in range(1,a+1):
    if a%i==0:
        print(i)