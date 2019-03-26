n = int(input())
arr = map(int, input().split())
arr = list(arr)
c = 0

last = n-1
for i in range(0,int(n/2)):
    cur = arr[i]
    arr[i] = arr[last]
    arr[last] = cur
    last -= 1
for i in range(0,n):
    print(arr[i])
