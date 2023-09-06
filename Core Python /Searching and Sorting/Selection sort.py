n=int(input())
arr=[int(i) for i in input().split()]
for i in range(0,n):  
   
    min1=i
    
    for j in range(i+1,n):   
        if arr[min1]>arr[j]: 
            min1=j  
    arr[i],arr[min1]=arr[min1],arr[i]
   
for i in arr:
    print(i,end=" ")
