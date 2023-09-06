
n=int(input())
arr=[int(i) for i in input().split()]
li=[]
ele=int(input())
count=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]==ele:
                li.append([arr[i],arr[j],arr[k]])
                count=count+1
print(li)
print(count)
