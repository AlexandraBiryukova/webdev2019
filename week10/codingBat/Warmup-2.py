def string_times(str, n):
  res=""
  for i in range(n):
    res+=str
  return res

def front_times(str, n):
  res=""
  str=str[:3]
  for i in range(n):
    res+=str
  return res

def string_bits(str):
  res=""
  for i in range(len(str)):
    if i%2==0:
      res+=str[i]
  return res

def string_splosion(str):
  res=""
  for i in range(1,len(str)+1):
    res+=str[:i]
  return res

def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[len(str)-2:]
  c = 0
  for i in range(len(str)-2):
    s = str[i:i+2]
    if s == last2:
      c = c + 1
  return c

def array_count9(nums):
  c=0
  for i in range(len(nums)):
    if nums[i]==9:
      c+=1
  return c

def array_front9(nums):
  if len(nums)>4:
    nums=nums[:4]
  for i in range(len(nums)):
    if nums[i]==9:
      return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2
    ]==3:
      return True
  return False

def string_match(a, b):
  s = min(len(a), len(b))
  c = 0
  for i in range(s-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      c = c + 1

  return c

