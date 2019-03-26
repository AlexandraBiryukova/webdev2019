n = int(input())
arr = map(int, input().split())
arr=list(arr)
for i in range(0,n):
    if arr[i]% 2 == 0:
        print(arr[i])