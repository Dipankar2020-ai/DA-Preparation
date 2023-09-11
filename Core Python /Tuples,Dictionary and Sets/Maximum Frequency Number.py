n=int(input())
li=[i for i in input().split()]

d={}
flag=False
for i in li:
    if i in d:
        d[i]=d[i]+1 
    else:
        d[i]=1 
max1=-1
pos=-1
for i in d:
    if d[i]>max1:
        max1=d[i]
        pos=i
print(pos)
