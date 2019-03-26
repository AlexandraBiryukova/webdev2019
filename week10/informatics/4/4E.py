arr = []
a = input()
a = int(a)
c = False
for i in range(0,a):
    arr.append(int(input()))
for i in range(1,a):
    if arr[i]*arr[i-1] > 0:
        print("YES")
        c = True
        break
if not c:
    print("NO")
