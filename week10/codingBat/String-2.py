def double_char(str):
  res=""
  for i in range(len(str)):
    res+=str[i]*2
  return res


def count_hi(str):
    c = 0
    for i in range(len(str) - 1):
        if str[i:i + 2] == "hi":
            c += 1
    return c

def cat_dog(str):
    c=0
    d=0
    for i in range(len(str)-2):
        if str[i:i+3]=='cat':
            c+=1
        if str[i:i+3]=='dog':
            d+=1
    return c==d

def count_code(str):
  c=0
  for i in range(len(str)-3):
    if str[i:i+2]=="co" and str[i+3]=="e":
      c+=1
  return c

def end_other(a, b):
  a=a.lower()
  b=b.lower()
  s=a
  f=b
  if len(a)>len(b):
    s=b
    f=a
  return f[len(f)-len(s):]==s

def xyz_there(str):
  for i in range(len(str)-2):
    if str[i:i+3]=="xyz":
      if i==0 or str[ i-1]!=".":
        return True
  return False
