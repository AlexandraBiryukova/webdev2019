from math import sqrt

a = input()
a = int(a)
c = 0
for i in range(1, int(sqrt(a))):
    if a % i == 0:
        c += 1
c*=2
if int(float(sqrt(a)))*int(float(sqrt(a)))==a:
    c+=1
print(c)