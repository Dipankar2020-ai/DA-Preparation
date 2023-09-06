n=int(input())
arr=[int(i) for i in input().split()]
ele=int(input())
start=0
end=n-1
while(start<=end):
    mid=(start+end)//2
    if (arr[mid]==ele):
        print("The element is present on {index}".format(index=mid))
        break 
    elif arr[mid]>ele:
        start=mid+1
    else:
        end=mid-1
else:
    print("The element is present on {index}".format(index=-1))
