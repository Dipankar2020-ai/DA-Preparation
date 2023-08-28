''' Rectangular pattern N=3
   
         33333
         32223
         32123
         32223
         33333
                     

'''

n=int(input())
value=n
size=2*n-1

a=[[0 for i in range(size)] for j in range(size)]

for i in range(n):
    for j in range(i,size-i):
        #vertical upper row
        a[i][j]=value
        #vertical lower row
        a[size-i-1][j]=value
        #horizontal left
        a[j][i]=value
        #horizontal right
        a[j][size-i-1]=value
    value-=1
for i in range(size):
    for j in range(size):
        print(a[i][j],end=" ")
    print()
        
    
