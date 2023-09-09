def countInString(str1):
    v,c,d,s=0,0,0,0
    for char in str1:
        if (char>='a' and char<='z') or (char>='A' and char<='Z'):
            char=char.lower()
            if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                v+=1
            else:
                c+=1 
        elif char>='0' and char<='9':
            d+=1
        else:
            s+=1 
    return v,c,d,s
str1="Dip@cse1"
v,c,d,s=countInString(str1)
print(v,c,d,s)
