#print sgr of even nos using lambda
n=[1,2,3,4,5,6]
x=list(filter(lambda a:a%2==0,n))
print(x)
p=list(map(lambda b:b**2,x))
print(p)


