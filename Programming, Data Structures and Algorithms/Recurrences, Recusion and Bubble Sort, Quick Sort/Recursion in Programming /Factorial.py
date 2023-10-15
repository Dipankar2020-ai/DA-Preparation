
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
        
print("Enter the number: ")
n=int(input())
print("Factorial of the number {0} is {1}".format(n,factorial(n)))


#Time complexity T(n)=c+T(n-1)---->O(n)
#Space Complexity O(n)
