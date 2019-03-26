n = int(input())
arr = map(int, input().split())
arr = list(arr)
c = False

for i in range(1,n):
    if arr[i]*arr[i-1] > 0:
        print("YES")
        c = True
        break
if not c:
    print("NO")
