x=[1,2,3,"four",5,"six",6,6,"seven","seven"]
print(x)
print(type(x))
print(len(x))
print("2" in x)
print(2 in x)
print("six" not in x)
#fetching value
print(x[3])
#fetch range of items
print(x[2:10])
print(x[2:])
print(x[:10])
print(x[-1])
print(x[-10:-2])
print(x[-2:])
print(x[:-2])
#modifications,changingvalues
x[9]="ten"
print(x)
#append
x.append("eleven")
print(x)
#insert
x.insert(1,"one")
print(x)
#extent
y=[11,12,13]
x.extend(y)
print(x)
#remove
x.remove(11)
print(x)
#POP
x.pop(5)
print(x)
x.pop()
print(x)
#del keyword
del x[3]
print(x)
#clear
# x.clear()
# print(x)
# del x
# print(x)
for i in x:
    print(i)

a=["one","xyz","mmm","kkk","abc","hgf"]
#print(a.sort())
a.sort()
print(a)
a.sort(reverse=True)
print(a)
#copy
b=a.copy()
print(b)
#copy using list
c=list(a)
print(c)
#join list
print(x+a)
#joinb using extend
x.extend(y)
print(x)
#count
print(x.count(12))
