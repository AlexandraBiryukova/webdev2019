from math import sqrt

a = input()
a = int(a)
i = 2
while i < a+1:
    if a%i==0:
        print(i)
        break
    i += 1
