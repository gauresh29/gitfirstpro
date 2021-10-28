list1=[a for a in range(50) if a%2==0]
print(list1)

set1={kalfa for kalfa in ['a','b','a','bsa']}
print(set1)

dict1={1:"item1",2:"item2",3:"item3",4:"item4"}
print(dict1)

compdic1={i:f"item{i}" for i in range(5)}
print(compdic1)

dict2 = {value:key for key,value in dict1.items()}
print( dict2)

gener = (i for i in range(n))
a = gener(5)
print(a.__next__())
