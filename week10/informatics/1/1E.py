a = input()
a1 = input()
a=int(a)
a1=int(a1)
if (a*a1==0):
    print(0)
if(a>0):
    print(a1*a%109)
else:
    print((109+((a1*a)%109))%109)
