arr = []
a = input()
a = int(a)
for i in range(0,a):
    arr.append(int(input()))
for i in range(0,a):
    if arr[i]% 2 == 0:
        print(arr[i])