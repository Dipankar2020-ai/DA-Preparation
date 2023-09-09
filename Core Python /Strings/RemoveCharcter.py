def removecharcter(str1,ch1):
    ans=""
    for i in range(len(str1)):
        
        if  str1[i]==ch1:
           continue
        else:
            ans=ans+str1[i]
    return ans
    
str1=input()
ch1=input()
str1=removecharcter(str1,ch1)
print(str1)
