arr = []
a = input()
a = int(a)
c = 0
for i in range(0,a):
    arr.append(int(input()))
for i in range(1,a-1):
    if arr[i] > arr[i-1]and arr[i]>arr[i+1]:
        c += 1
print(c)
