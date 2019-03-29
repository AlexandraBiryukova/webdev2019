def count_evens(events):
  c=0
  for i in range(len(events)):
    if events[i]%2==0:
      c+=1
  return c

def big_diff(nums):
  return max(nums)-min(nums)


def centered_average(nums):
    maxi = max(nums)
    mini = min(nums)
    foundmaxi = False
    foundmini = False
    sum = 0
    c = 0
    for i in range(len(nums)):
        if nums[i] != maxi and nums[i] != mini:
            sum += nums[i]
            c += 1
        else:
            if foundmaxi and nums[i] == maxi:
                sum += maxi
                c += 1
            if foundmini and nums[i] == mini:
                sum += mini
                c += 1
            if not foundmaxi and nums[i] == maxi:
                foundmaxi = True
            if not foundmini and nums[i] == mini:
                foundmini = True
    return sum // c

def sum13(nums):
  sum=0
  if len(nums)==0:
    return 0
  for i in range(1,len(nums)):
    if nums[i]!=13 and nums[i-1]!=13:
      sum+=nums[i]
  if nums[0]!=13:
    sum+=nums[0]
  return sum

def sum67(nums):
  record = True
  total = 0
  for n in nums:
    if n == 6:
      record = False

    if record:
      total += n
      continue

    if n == 7:
      record = True

  return total

def has22(nums):
  if len(nums)>=2:
    for i in range(len(nums)-1):
      if nums[i]==2 and nums[i+1]==2:
        return True
  return False