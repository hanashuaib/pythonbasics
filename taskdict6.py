d={1:0,"my":1,"name":2,"is":3,"hana":4,2:5,"and":6,"im":7,"from":8,"edpl":9}
print(d)
print(len(d))
print(type(d))
for i in d:
    print(i)
print("hana" in d)
print("is" not in d)    
print(d["my"])
print(d[1])
x=d.get("hana")
print(x)
print(d.keys())
print(d.values())
print(d.items())
d["hana"]=20
print(d)
d.update({"my":10})
print(d)
d["hana"]="hp"
print(d)
d.update({"ww":15})
print(d)
d.pop("ww")
print(d)
p=d.popitem()
print(d)
print(p)
del d["from"]
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
cl={"student1":{"name":"arjun","no":1,"age":20},"student2":{"name":"seetha","no":2,"age":19},
       "student3":{"name":"arya","no":3,"age":21}} 
print(cl) 
print(cl["student1"])
print(cl["student2"]["name"])
print(cl["student1"]["name"])

         