set={1,2,3,4,5,6,8,"sss","yyy"}
print(set)
print(type(set))
print(len(set))
print(1 in set)
print(11 not in set)
for i in set:
    print(i)
set.add("hp")
print(set)    
a={33,444,555}
set.update(a)
print(set)
list=[20,30]
set.update(list)
print(set)
set.remove("hp")
print(set)
set.discard(00)
print(set)
set.discard(1)
print(set)
x=set.pop()
print(set)
print(x)
#set.clear()
#print(set)
#del set
#print(set)
y=a.union(set)
print(y)
u={1,2,3,4,5}
c=set.intersection(u)
print(c)
b=set.difference(c)
print(b)
