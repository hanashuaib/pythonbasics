#blocks
try:
    # print(x)
    print("33")
except NameError:
    print("define the variable")    
except:
    print("there is an error") 
else:
    print("no error")
finally:
    print("completed successfully")    
#raise or throw error/exception
x=-3
if x<0:
    raise Exception("no number lessthan 0 is allowed")
