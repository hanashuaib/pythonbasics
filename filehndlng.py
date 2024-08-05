import os

x=open("filehandling.txt","r")
print(x.read())
x.close()
y=open("filehandling.txt","r")
print(y.read(20))
y.close()
#linebyline read
z=open("filehandling.txt","r")
print(z.readline())
print(z.readline())
print(z.readline())
z.close()
# a=open("filehandling.txt","a")
# # a.write("\naaaaaaaaassss\nssssssssssdddnmnbmnm")
# a.close()
# a=open("filehandling.txt","w")
# a.write("abcdefghijklmnopqrstuvwxyz")
# a.close()

#to creste new file
# b=open("newfile.txt","x")

#delete file
# os.remove("newfile.txt")

#directory management
# os.rmdir("directory")   #to remove the folder



