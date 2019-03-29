def first_last6(nums):
  if nums[0]==6 or nums[len(nums)-1]==6:
    return True
  return False

def same_first_last(nums):
  if len(nums)>0 and nums[0]==nums[len(nums)-1]:
    return True
  return False

def make_pi():
  return [3,1,4]

def common_end(a, b):
  if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
    return True
  return False

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  c=nums[0]
  nums.remove(nums[0])
  nums.append(c)
  return nums

def reverse3(nums):
  return list(reversed(nums))

def max_end3(nums):
  arr=[]
  for i in range(3):
    arr.append(max(nums[0],nums[len(nums)-1]))
  return arr

def sum2(nums):
  if len(nums)<=2:
    return sum(nums)
  return nums[0]+nums[1]

def middle_way(a, b):
  return [a[1],b[1]]

def make_ends(nums):
  return [nums[0],nums[len(nums)-1]]

def has23(nums):
  a=2
  b=3
  if nums[0]==2 or nums[0]==3 or nums[1]==2 or nums[1]==3:
    return True
  return False