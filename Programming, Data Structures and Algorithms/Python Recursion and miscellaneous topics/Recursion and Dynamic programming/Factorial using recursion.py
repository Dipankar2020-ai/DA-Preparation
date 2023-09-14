#Factorial using Recursion

def factorial(n):
    if n<0:
        return "Error"
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
        
        
n=int(input())
print("factorial of {0} is {1}".format(n,factorial(n)))
