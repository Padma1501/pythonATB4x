### Task #5



"""- Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.


Ex:

num1 =int(input("Enter the num1"))
num2 =int(input("Enter the num2"))
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)

"""

num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")
