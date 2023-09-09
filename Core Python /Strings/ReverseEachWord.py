def revereEachword(str1):
    list1=[i for i in str1.split()]
    list2=[]
    for i in range(len(list1)):
        list1[i]=list1[i][::-1]
        list2.append(list1[i])
    return list2
str1=input()
list1=revereEachword(str1)
for i in list1:
    print(i,end=" ")
