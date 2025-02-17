"""
TASK #2
create a program using 2 user inputs num1 and num2
1. max
2. pow num1 to num2
3. sub, mul, div, sum
4. format your output with f"{}"

"""

num1 = int(input("enter the number1")) # num1= 10
num2 = int(input("enter the number2")) # num2= 20
print(type(num1))
print(type(num2))
print(max(num1, num2))
print("sum is", num1+num2)
print("sub is", num1-num2)
print("div is", num1/num2)
print("mul is", num1*num2)
print(f"{num1}")