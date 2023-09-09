def checkpermmutation(str1,str2):
    if len(str1)==len(str2):
        sum1=0
        sum2=0
        for i in range(len(str1)):
            sum1+=ord(str1[i])
        for j in range(len(str2)):
            sum2+=ord(str2[j])
        if sum1==sum2:
            return True
        else:
            return False
            
        
    else:
        return False

str1=input()
str2=input()
print(checkpermmutation(str1,str2))
