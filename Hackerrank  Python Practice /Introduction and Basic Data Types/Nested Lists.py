#Link-https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
'''harry 37.21
00    01
berry 37.21
10     11
tina  37.2
20      21
akriti  41
30      31 '''

n=int(input())
li=[]
for i in range(n):
    a=input()
    b=float(input())
    li.append([a,b])
li2=[]
for i in range(n):
    li2.append(li[i][1])
#print(li2)
sl=set(li2)
li2=list(sl)
li2.sort()

#print(li2)
li3=[]
for i in range(n):
    if li[i][1]==li2[1]:
        li3.append(li[i][0])
#print(li3)
li3.sort()
#print(li3)
for i in li3:
    print(i)   
    
    


