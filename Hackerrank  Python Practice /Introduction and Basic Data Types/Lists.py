#List-https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
n=int(input())
li=[]
for i in range(n):
    a=[i for i in input().split()]
    if a[0]=="insert":
        li.insert(int(a[1]),int(a[2]))
    if a[0]=="print":
        print(li)
    if a[0]=="remove":
        li.remove(int(a[1]))
    if a[0]=="append":
        li.append(int(a[1]))
    if a[0]=="sort":
        li.sort()
    if a[0]=="pop":
        li.pop()
    if a[0]=="reverse":
        li.reverse()

    
