def sample():
    print("this is a funtion")
sample()

def parameter(x):
    print("parameter is passed",x)
parameter(10) 

#sum of two no.
def addition(x,y):
    print("sum of two number",x+y)
addition(3,5)    
#arbitrary arg
def arbitrary(*x):
    print(x[2])
arbitrary(1,2,3,4,5,"sdf")    
#keyword args
def keyword(x,y,z):
    print(y)
keyword(x="apple",y="mango",z="kiwi")       
#arbitrary keyword args
def arbitrarykwargs(**x):
    print(x["a"])
arbitrarykwargs(a="sss",b=1,c=3)
#default
def dfp(country="india"):
    print(country)
dfp("uk")        
dfp()
#list as arg
l=[1,2,3,4,5]
def list(x):
    for i in x:
        print(i)
list(l)        
#return funtion
def returnf(x):
    return x+5
print(returnf(20))
#funtion can be passed
def passed():
    pass
#recursion
#factorial using recursion
