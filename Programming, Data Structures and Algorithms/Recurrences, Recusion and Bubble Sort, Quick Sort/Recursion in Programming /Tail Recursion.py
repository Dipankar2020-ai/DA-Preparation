# Tail Recursion
def factorial(n,a):  #Accumulator
    
    if n==0 or n==1:
        return a
    else:
        return factorial(n-1,n*a)
n=int(input())
a=int(input())
print(factorial(n,a))

#After Recursion return original function , no operations need to be performed
#Space complexity-O(1) [no need of call stack]
