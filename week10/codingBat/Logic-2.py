def make_bricks(small, big, goal):
    if (big != 0 and goal / 5 == big and goal % (big * 5) == 0) or (small != 0 and small > goal):
        return True
    if goal == 0:
        return True
    if (goal / 5 <= big and (goal - big * 5) % 5 <= small):
        return True
    if 0 <= (goal - big * 5) <= small and big != 0:
        return True
    return False


def lone_sum(a, b, c):
    if a == b:
        if a == c:
            return 0
        return c
    if a == c:
        return b
    if b == c:
        return a
    return (a + b + c)

def lucky_sum(a, b, c):
  if a==13:
    return 0
  if b==13:
    return a
  if c==13:
    return a+b
  return a+b+c


def fix_teen(n):
    if 19 >= n >= 13 and n != 15 and n != 16:
        return 0
    return n
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def round10(n):
    if n % 10 >= 5:
        return n + 10 - n % 10
    return n - n % 10
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def close_far(a, b, c):
  return abs(b-a) <= 1 and abs(c-a) >= 2 and abs(c-b) >= 2 or abs(c-a) <= 1 and abs(b-a) >= 2 and abs(b-c) >= 2

def make_chocolate(small, big, goal):
  maxBig = goal/5
  if maxBig <= big:
    goal -= maxBig*5
  else:
    goal -= big*5
  if goal <= small:
    return goal
  return -1

