#input-
#1
#7
#2 3 1 6 3 6 2
#Output-1

t=int(input())

while t>0:
    n=int(input())
    li=[int(i) for i in input().split()]
    for i in range(n):
        if li.count(li[i])==1:
            print(li[i])
    t-=1
