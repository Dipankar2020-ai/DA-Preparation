n1=int(input())
arr1=[int(i) for i in input().split()]
n2=int(input())
arr2=[int(i) for i in input().split()]

i=0
j=0
arr3=[]
while i<n1 and j<n2:
    if arr1[i]>arr2[j]:
        arr3.append(arr2[j])
        j+=1
    else:
        arr3.append(arr1[i])
        i+=1
while i<n1:
    arr3.append(arr1[i])
    i+=1
while j<n2:
    arr3.append(arr2[j])
    j+=1
print(arr3)
