def checkPalindrome(n):
    temp=n
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    
    if rev==temp:
        return True
    else:
        return False

n=int(input())

if checkPalindrome(n):
    print("True")
else:
    print("False")
