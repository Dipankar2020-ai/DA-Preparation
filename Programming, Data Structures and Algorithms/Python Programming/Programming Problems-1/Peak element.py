#Link-https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/find-any-of-the-peak-elements/problem
def maxneighbourfound(li):
    
    maxneighbour=-10000
    pos=-1
    n=len(li)
    flag=False
    for i in range(1,n):
        if li[i]>li[i-1] :
            maxneighbour=li[i]
            pos=i
            flag=True
    if flag==False:
        return 0
    else:
        return pos
        
        
li=[int(i) for i in input().split(',')]
ans=maxneighbourfound(li)
print(ans)
