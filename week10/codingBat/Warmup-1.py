def sleep_in(weekday, vacation):
  if weekday is False or vacation is True:
    return True
  return False

def monkey_trouble(a_smile, b_smile):
  if (a_smile is True and b_smile is True):
    return True
  if(a_smile is False and b_smile is False):
    return True
  return False

def sum_double(a, b):
  res=a+b
  if a==b:
    res*=2
  return res

def diff21(n):
  if n<=21:
    return abs(21-n)
  return 2*abs(21-n)

def parrot_trouble(talking, hour):
  if talking and (hour<7 or hour>20):
    return True
  return False

def makes10(a, b):
  if a==10 or b==10 or a+b==10:
    return True
  return False

def near_hundred(n):
  if abs(100-n)<=10 or abs(200-n)<=10:
    return True
  return False

def pos_neg(a, b, negative):
  if negative is True:
    if a<0 and b<0:
      return True
  else:
    if a*b<0:
      return True
  return False

def not_string(str):
  if str[:3]!= "not":
    str="not "+str
  return str

def missing_char(str, n):
  return str[:n]+str[(n+1):]

def front_back(st):
  if len(st)>1:
    return st[len(st)-1]+st[1:(len(st)-1)]+st[0]
  return st

def front3(str):
  if len(str)<=3:
    return str+str+str
  return str[:3]+str[:3]+str[:3]
