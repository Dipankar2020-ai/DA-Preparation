def removeconsecutive(str1):
    length=len(str1)
    ans=""
    ans=ans+str1[0]
    for i in range(1,length-1):
        if str1[i]!=ans[-1]:
            ans=ans+str1[i]
    return ans
        
                
           
            
    

str1=input()
str1=removeconsecutive(str1)
print(str1)
