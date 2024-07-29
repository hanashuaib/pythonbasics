# #sum of first 10 natural numbers using for loop in python
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)
# #sum of even numbers in range of 1 to 20
# sum=0
# for i in range(1,20,2):
#     sum=sum+i
# print(sum)
# #factorial of a number
# fact=1
# n=int(input ("enter the number "))
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial of",n,"is",fact)
# #sum of square of first 10 natural numbers
# sum=0
# for i in range(1,11):
#      sum+=i*i
# print("sum of square is ",sum)  
#check whether a number is prime or not
num=int(input("enter the number "))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not prime")
            break
    else: 
        print(num,"is prime") 
else:
    print(num,"is not prime")        