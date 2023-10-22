
def selectionsort(arr):
    for i in range(len(arr)):
        min_ele_index =i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_ele_index]:
                min_ele_index=j
        #Swap
        arr[i],arr[min_ele_index]=arr[min_ele_index],arr[i]
arr=[int(i) for i in input().split()]
selectionsort(arr)
for v in arr:
    print(v,end=" ")
