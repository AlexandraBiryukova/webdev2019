arr = []
a = input()
a = int(a)
c = 0
for i in range(0,a):
    arr.append(int(input()))
last = a-1
for i in range(0,int(a/2)):
    cur = arr[i]
    arr[i] = arr[last]
    arr[last] = cur
    last -= 1
for i in range(0,a):
    print(arr[i])
