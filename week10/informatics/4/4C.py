n = int(input())
arr = map(int, input().split())
arr = list(arr)
c = 0
for i in range(0,n):
    if arr[i] > 0:
        c += 1
print(c)
