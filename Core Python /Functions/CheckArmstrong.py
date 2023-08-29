def checkArmstorng(n):
    temp1=n
    temp2=n
    count=0
    total=0
    while(n>0):
        count+=1
        n=n//10
 
    while temp1>0:
        rem=temp1%10
        total+=rem**count
        temp1=temp1//10
    
    if total==temp2:
        return True
    else:
        return False
   
    
n=int(input())
if checkArmstorng(n):
    print("True")
else:
    print("False")
