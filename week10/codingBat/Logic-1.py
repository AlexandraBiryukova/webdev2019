def cigar_party(cigars, is_weekend):
  if is_weekend:
     return 40<=cigars
  else:
    return 40<=cigars<=60
  return False

def date_fashion(you, date):
  if you<=2 or date<=2:
    return 0
  elif you>=8 or date>=8:
    return 2
  return 1

def squirrel_play(temp, is_summer):
  if is_summer:
    return 60<=temp<=100
  else:
    return 60<=temp<=90
  return False

def caught_speeding(speed, is_birthday):
  s=60
  f=80
  if is_birthday:
    s+=5
    f+=5
  if speed<=s:
    return 0
  elif f>=speed>=s+1:
    return 1
  return 2

def sorta_sum(a, b):
  res=a+b
  if 19>=res>=10:
    return 20
  return res

def alarm_clock(days, vacation):
  if vacation:
    if days==0 or days==6:
      return "off"
    return "10:00"
  else:
    if days==0 or days==6:
      return "10:00"
  return "7:00"

def love6(a, b):
  if a==6 or b==6 or a+b==6 or abs(a-b)==6:
    return True
  return False

def in1to10(n, outside_mode):
  if outside_mode:
    return 1>=n or n>=10
  return 10>=n>=1

def near_ten(num):
  if (num%10)<=2 or (num+2)%10<=2:
    return True
  return False