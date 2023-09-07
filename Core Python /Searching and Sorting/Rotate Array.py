n=int(input())
arr=[int(i) for i in input().split()]
r=int(input())
#Approach 1
for i in range(r):
    key=arr[0]
    for j in range(n-1):
        arr[j]=arr[j+1]
    arr[j+1]=key
print(arr)
