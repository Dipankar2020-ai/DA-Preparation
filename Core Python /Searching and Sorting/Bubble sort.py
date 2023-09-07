n=int(input())
arr=[int(i) for i in input().split()]
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
