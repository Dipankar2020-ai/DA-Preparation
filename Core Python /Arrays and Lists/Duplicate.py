n=int(input())
li=[int(x) for x in input().split()]
sum1=0
for i in range(n):
    sum1=sum1+li[i]
sum2=((n-1)*(n-2))//2
print(abs(sum2-sum1))
