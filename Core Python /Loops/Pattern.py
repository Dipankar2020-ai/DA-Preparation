
''' Pattern:
        1
       232
      34543
     4567654 '''



n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end=" ")

        
    
    k=i
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    p=2*(i-1)
    for j in range(i,1,-1):
        print(p,end=" ")
        p=p-1
    print("")
