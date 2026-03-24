List=['a',1,'b',20.22,False]
print(List)
print(type(List[0]))
print(type(List[1]))
print(type(List[3]))
print(type(List[4]))

Tuple=(1,2,3,4,5)
#Tuple[2]=100  #error

Set={1,2,3,4,5}
Set.add(10)
print(Set)
Set.add(2)
print("After adding 2 again",Set)  #unique values concept

dict={'a':1,'b':2,'c':3,'e':20.5}
print("Dictionary",dict['a'])
del dict['b']
print("Dictionary after delete",dict)