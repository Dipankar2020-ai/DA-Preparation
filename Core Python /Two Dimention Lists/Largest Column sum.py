str1=input().split()
n,m=int(str1[0]),int(str1[1])
li=[[int(j) for j in input().split()] for i in range(n)]
maximum=-1
for i in range(m):
    sum2=0
    for j in range(n):
        
        sum2=sum2+li[j][i]
    maximum=max(sum2,maximum)
print(maximum)

for i in range(m):
    sum2=0
    for j in range(n):
        
        sum2=sum2+li[j][i]
    if sum2==maximum:
        print(i)
