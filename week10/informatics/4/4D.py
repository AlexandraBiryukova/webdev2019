
c = 0
n = int(input())
arr = map(int, input().split())
arr = list(arr)
for i in range(1,n):
    if arr[i] > arr[i-1]:
        c += 1
print(c)
