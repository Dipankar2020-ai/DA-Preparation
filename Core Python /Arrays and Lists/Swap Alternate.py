#Input-
# 1
# 6
#9 3 6 12 4 32
#3 9 12 6 32 4

t=int(input())
while t>0:
    n=int(input())
    li=[int(i) for i in input().split()]
    for i in range(0,n,2):
        if i<n-1:
            li[i],li[i+1]=li[i+1],li[i]
    print(li)
    t-=1
