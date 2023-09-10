def sum1(a,b,*more):
    sum1=a+b
    for i in more:
        sum1=sum1+i
    return sum1
    
print(sum1(1,2,3,4,5,6))
