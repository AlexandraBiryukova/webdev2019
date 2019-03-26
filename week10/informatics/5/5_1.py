def is_a_palindrome(str):
    last=len(str)-1
    for i in range(0,int(len(str)/2)):
        if str[i]!=str[last]:
            return False
        last -= 1

    return True

s=input()
if(is_a_palindrome(s)):
    print("YES")
else:
    print("NO")
