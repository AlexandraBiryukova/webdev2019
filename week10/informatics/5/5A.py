def minimum(a, b, c, d):
    return min(d,min(c, min(a,b)))


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(minimum(a, b, c, d))