arr = []
a = input()
a = int(a)
c=0
for i in range(0,a):
    arr.append(int(input()))
for i in range(0,a):
    if arr[i] > 0:
        c += 1
print(c)
