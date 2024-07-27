i=1
while i<=10:
    print(i)
    i+=1
#increment by 2    
i=1
while i<=20:
    print(i)
    i+=2    
#break
i=1
while i<=10:
    print(i)
    
    if i==5:
        break 
    i+=1
#continue    
i=0
while i<=10:
    i+=1
    if i==5:
        continue
    print(i)    
#for
s=(1,2,"aa","bb")
for i in s:
    print(s)
l=[11,22,33,"ccc"]   
for i in l:
    if i==33:
        break
    print(l)
t=("hh","pp",20,21,23,55)
for i in t:
    print(t)
s={10,11,12,13}
for i in s:
    print(s)
d={"hp":1,"pp":28,"ui":50,222:9} 
for i in d:
    print(d)
#for  range
for i in range(11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
#break            
l=[11,22,33,"ccc"]   
for i in l:
    if i==33:
        break
    print(i)
#continue
l=[11,22,33,"ccc"]   
for i in l:
    if i==22:
        continue
    print(i)
#pass statement    
for i in range(2):
    pass        
#nested for loop
list=["ss","dd","ddd8","www","rrr"]
tuple=(1,2,3,4,5,6,7,8)
for i in list:
    for j in tuple:
        print(i,j)