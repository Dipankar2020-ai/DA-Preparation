
#Lambda Function using filter
import functools
lst=[1,2,3,4,5,6]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)

#lambda Function using map

lst1=[1,2,3,4,5,6]
new_lst=list(map(lambda x:x**2,lst1))
print(new_lst)

#lambda Function using reduce
lst2=[1,2,3,4,5,6]
new_lst2=functools.reduce(lambda x,y:x*y,lst2)
print(new_lst2)
