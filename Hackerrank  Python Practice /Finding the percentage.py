n=int(input())
li=[]
for i in range(n):
        
    a=[i for i in input().split()]
    b=a[0]
    c=[float(i) for i in a[1:]]
    li.append([b,c])
value=input()
for i in range(n):
    if li[i][0]==value:
        ans=sum(li[i][1])/len(li[i][1])
ans=format(ans,".2f")
print(ans) 
