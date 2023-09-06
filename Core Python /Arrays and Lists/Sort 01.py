n=int(input())
arr=[int(i) for i in input().split()]
zeropos=0
current=0
while current<len(arr):
    if arr[current]==0:
        arr[current],arr[zeropos]=arr[zeropos],arr[current]
        zeropos=zeropos+1
    current=current+1
for i in arr:
    print(i,end=" ")
