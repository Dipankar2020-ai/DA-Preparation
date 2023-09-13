#Link-https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/fizz-buzz-11/problem
n=int(input())
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        if i==n:
            print("FizzBuzz",end="")
        else:
            print("FizzBuzz",end=",")
            
    elif i%3==0:
        if i==n:
            print("Fizz",end="")
        else:
            print("Fizz",end=",")
            
    elif i%5==0:
        if i==n:
            print("Buzz",end="")
        else:
            print("Buzz",end=",")
    
    else:
        if i==n:
             print(i,end="")
        else:
            
            print(i,end=",")
