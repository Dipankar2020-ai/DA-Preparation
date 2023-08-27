'''
   Pattern:
          1234
           234 
            34 
             4 
            34 
           234 
          1234

'''

t=int(input())
n=t 
m=t-1

for i in range(1,n+1):
    k=i
    for j in range(1,i):
        print(" ",end=" ")
    for j in range(n,i-1,-1):
        print(k,end=" ")
        k=k+1
    print(" ")

for i in range(1,m+1):
    k=m-i+1
    for j in range(m,i,-1):
         print(" ",end=" ")
    for j in range(0,i+1):
        
            print(k,end=" ")
            k=k+1 
    print("")
