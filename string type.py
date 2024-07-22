x="hello"
print(x)
print(type(x))
print(len(x))
y="python is, a programming, language"
print(len(y))
#to check a sequence present or not membership operator
print("is" in y)
print("hello" in y)
print("is" not in y)
print("xyx" not in y)
#for loop (iteration)
for i in y:
    print(i)
#access character from position value    
print(y[5])        
#slicing(range of index position,to extractcharacters)
print(y[1:3])
#only stsrting position mentioned
print(y[5:])
#ending only specified
print(y[:6])
#negative indexing to fetch last character
print(y[-3])
print(y[-5:-1])
print(y[:-10])
print(y[-10:])
#string to uppercase
print(x.upper())
print(x.lower())
#replace character
print(y.replace("is","was"))
#split
print(y.split(","))
#concatenation
print(x+y)
# to have space in between
print(x+" "+y)
#inpython number and string cannot be concatenate, so use "format"
age=20
a=f"my name is anu and iam {age}"
print(a)
#count 
print(a.count("a"))