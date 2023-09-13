#Link-https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges
def sumofnumbers(list,n):
    
    sum=0
    for i in list:
        
        sum=sum+i
    return sum

n=int(input())
if n==0:
    print('0')
else:
    list=[int(i) for i in input().split()]
    ans=sumofnumbers(list,n)
    print(ans)
