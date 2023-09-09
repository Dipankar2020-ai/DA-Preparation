def replacecharacter(str1,char1,char2):
    str2=""
    for i in range(len(str1)):
        if str1[i]==char1:
            str2=str2+char2
        else:
            str2=str2+str1[i]
            
    return str2

str1="Dipankar"
str1=replacecharacter(str1,'a','b')
print(str1)
