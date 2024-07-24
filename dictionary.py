d={"hello":1,"world":2,1:9,66:3}
print(d)
print(len(d))
print(type(d))
print(1 in d)
print(1 not in d)
for i in d:
    print(i)
print(d[1])    
print(d["world"])
x=d.get("world")
print(x)
print(d.keys())
print(d.values())
print(d.items())
d["hello"]="8"
print(d)
d.update({"world":50})
print(d)
d["mm"]=0
print(d)
d.update({"to":7})
print(d)
d.pop("to")
print(d)
d.popitem()
print(d)
del d[1]
print(d)
# d.clear()
# print(d)
# del d
# print(d)
for i in d:
    print(d[i])
for i in d.keys():
    print(i)
for i in d.values():
    print(i)        
for i in d.items():
    print(i)
c=d.copy()
print(c)
x=dict(d)
print(x)

family={"child1":{"name":"arya","age":20},"child2":{"name":"amal","age":21},"child3":{"name":"anu","age":22}}
print(family)
print(family["child1"])
print(family["child2"]["age"])
print(family["child3"]["name"])
