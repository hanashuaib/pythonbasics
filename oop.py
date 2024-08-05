class animal:
    x=10
obj=animal()
print(obj.x)    

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=person("hana",22)
print(obj.name,obj.age)       

#inheritance
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def place(self):
        print(self.name,self.age) 
class student(person):
    pass
obj=student("helen",23)
obj.place()

#class polymorphism
class car:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def movement(self):
        print("drive")
class plane:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def movement(self):
        print("fly")
obj1=car("innova","black")
obj2=plane("indianairline","white")        
obj1.movement()
obj2.movement()
print(obj1.name)


