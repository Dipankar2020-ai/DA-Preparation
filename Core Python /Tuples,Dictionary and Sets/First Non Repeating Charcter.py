
w=input()
d={}
for i in w:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d:
    if d[i]==1:
        print(i)
        break
