a=input()
b=input()
c=input()
d=input()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=""
for i in range(a,b+1):
    if i%d==c:
        e+=str(i)+" "
print(e)