'''
  Diamond Pattern-
           *
          ***
         *****
          ***
           *

'''

m=int(input())
n1=(m+1)//2
n2=m-n1

for i in range(1,n1+1):
    p=2*i-1
    for j in range(n1,i,-1):
        print(" ",end=" ")
        
    for j in range(1,p+1):
        print("*",end=" ")
    print(" ")
    
for i in range(1,n2+1):
    for j in range(0,i):
        print(" ",end=" ")
    h=n2-i+1
    for j in range(1,2*h):
        print("*",end=" ")
    print(" ")
