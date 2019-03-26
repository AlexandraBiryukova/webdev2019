def XOR(x,y):
    res=False
    if (x==True and y==True) or(x==False and y==False):
        res=True
    return res


a=input()
b=input()
a=bool(a)
b=bool(b)
print(a)
print(b)

if XOR(a, b):
    print(0)
else:
    print(1)