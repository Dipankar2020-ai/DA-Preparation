import math
def fartocel(start,end,step):
    for i in range(start,end+1,step):
        ans=math.trunc((5*(i-32))/9)
        print("{a} {b}".format(a=i,b=ans))

start=int(input())
end=int(input())
step=int(input())
fartocel(start,end,step)
