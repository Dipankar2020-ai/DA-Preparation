def insertionsort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
        
n=int(input())
arr=[int(i) for i in input().split()]
insertionsort(arr,n)
print(arr)
