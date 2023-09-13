#Link-https://www.hackerrank.com/contests/diploma-in-ai-and-ml-uoh/challenges/find-the-second-largest-element-in-an-list/problem

def secondlargest(li,length):
    max=li[0]
    flag=False
    for i in li[1:]:
        if i>max:
            max=i
    secondmax=-10000
    for i in li[:]:
        if i>secondmax and i<max:
            secondmax=i
            flag=True
    if flag==False:
        return "Error"
            
    return secondmax
    




list=[int(i) for i in input().split(',')]
length=len(list)

if length>=2:
    print(secondlargest(list,length))
