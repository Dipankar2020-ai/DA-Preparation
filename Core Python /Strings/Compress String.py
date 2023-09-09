
str1=input()
ans=""
ans=ans+str1[0]
count=1
length=len(str1)
i=1
while i<length:
    if str1[i]==ans[-1]:
        count+=1
    else:
        if count>1:
            ans=ans+str(count)+str1[i]
            count=1
        else:
            ans=ans+str1[i]
            count=1
        
    i+=1
else:
    ans=ans+str(count)
print(ans)
