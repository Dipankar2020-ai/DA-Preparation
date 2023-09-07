n=int(input())
arr=[int(i) for i in input().split()]
#Approach 2
max1=arr[0]
for i in range(n):
    if arr[i]>max1:
        max1=arr[i]
secondmax=arr[0]
for i in range(n):
    if arr[i]>secondmax and arr[i]<max1:
        secondmax=arr[i]
print(secondmax)
