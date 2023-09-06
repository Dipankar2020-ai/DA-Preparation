n=int(input())
li=[int(x) for x in input().split()]
ans=li[0]
for i in range(1,n):
    ans=ans ^ li[i]
print("Unique Number is " ,ans)
