
n=int(input())
li=[int(x) for x in input().split()]
length=len(li)
for i in range(length//2):
    li[i],li[length-i-1]=li[length-i-1],li[i]
print(li)
