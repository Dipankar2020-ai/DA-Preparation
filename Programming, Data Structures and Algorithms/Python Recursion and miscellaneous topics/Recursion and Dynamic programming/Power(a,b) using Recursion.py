# Power of (a,b) using recursion
import math

def Powerof(a,b):
    if b==0:
        return 1
    if b%2==0:
        temp=Powerof(a,b/2)
        return temp*temp
    else:
        temp=Powerof(a,math.floor(b/2))
        return temp*temp*a
       
a=int(input())
b=int(input())

print("The power of {a1} to the power {b1} is {result}".format(a1=a,b1=b,result=Powerof(a,b)))
