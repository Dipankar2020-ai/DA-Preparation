#Link-https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
n=int(input())
li=[int(i) for i in input().split()]
se=set(li)
a=list(se)
a.sort()
print(a[-2])
