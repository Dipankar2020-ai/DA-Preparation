w=input()
d={}
for i in w:
    d[i]=d.get(i,0)+1

for i in d:
    print(i,end='')
