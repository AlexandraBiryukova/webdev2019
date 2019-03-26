a=input()
b=input()
a=int(a)
b=int(b)
c=""
for i in range(a,b+1):
    if i%2==0:
        c+=str(i)+" "
print(c)