#Check prime
def isprime(n):
    flag=False
    for i in range(2,n):
        if n%i==0:
            flag=True
            break 
    return flag
    
n=int(input())

if isprime(n):
    print("Not Prime")
else:
    print("Prime")
