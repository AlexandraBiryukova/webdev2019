from math import sqrt

a = input()
a = int(a)
i = 1
while i < a:
    i *= 2
if i == a:
    print("YES")
else:
    print("NO")
