# #using function print sum of n numbers
# def sum():
#     n=int(input("enter the number "))
#     s=0
#     for i in range(1,n):
#         s=s+i
#     print(s)
# sum()
# # using function print fibonacci series
# n=int(input("enter the number"))
# def fibonaccis(x):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(1,x):
#         c=a+b
#         print(c)
#         a = b
#         b = c
# fibonaccis(n) 

# #calculate the product and sum of two numbers(num1=20,num2=30)
# def calculate_sum(num1, num2):
#     return num1 + num2
# def calculate_product(num1, num2):
#     return num1 * num2
# num1 = 20
# num2 = 30
# sum_result = calculate_sum(num1, num2)
# product_result = calculate_product(num1, num2)
# print(f"The sum of {num1} and {num2} is: {sum_result}")
# print(f"The product of {num1} and {num2} is: {product_result}")

# #calculate average of 30,100,2000
# def calculate_average(numbers):
#     sum_numbers = 0
#     for num in numbers:
#         sum_numbers += num
#     average = sum_numbers / len(numbers)
#     return average
# numbers = [30, 100, 2000]
# average = calculate_average(numbers)
# print(average)  

# #create a function that takes an integer n as input and return the sum of all numbers from 1 to n .use a loop
# def sum_from_1_to_n(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum
# n = 10
# result = sum_from_1_to_n(n)
# print("The sum of all numbers from 1 to", n, "is:", result)

# # create a function that checks whether a given number is prime or not. return true if its prime,otherwise false
 
# def is_prime(number):
#     if number <= 1:
#         return False
#     if number <= 3:
#         return True
#     if number % 2 == 0 or number % 3 == 0:
#         return False
#     i = 5
#     while i * i <= number:
#         if number % i == 0 or number % (i + 2) == 0:
#             return False
#         i += 6
    
#     return True
# number = int(input("enter number "))
# result = is_prime(number)
# print(f"The number {number} is prime: {result}")

# #function to calculate the factorial of a given number
# def factorial():
#     n=int(input ("enter the number "))
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print("factorial of",n,"is",f)
# factorial()

#leap year or not
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
