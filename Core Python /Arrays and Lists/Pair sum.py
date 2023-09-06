n=int(input())
arr=[int(x) for x in input().split()]
ele=int(input())
li=[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==ele:
            li.append([arr[i],arr[j]])
for i in range(len(li)):
    print(li[i][0],li[i][1])
