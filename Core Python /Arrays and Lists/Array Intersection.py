n1=int(input())
arr1=[int(x) for x in input().split()]
n2=int(input())
arr2=[int(y) for y in input().split()]
li=[]


for i in range(n1):
    for j in range(n2):
        if arr1[i]==arr2[j]:
            li.append(arr1[i])
for i in li:
    print(i)
