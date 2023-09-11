li=[i for i in input().split()]
d={}
flag=False
for i in li:
    if i in d:
        d[i]=d[i]+1 
    else:
        d[i]=1 
for i in d:
    if d[i]>1:
        print(i," ",d[i])
        flag=True
if flag==False:
    print(-1)
