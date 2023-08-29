#Prime2toN
def isprime(n):
    flag=False
    for i in range(2,n):
        if n%i==0:
            flag=True
            break 
    return flag
def prime2toN(n):
    for i in range(2,n+1):
        if isprime(i)==False:
            print(i)
    
n=int(input())
prime2toN(n)
