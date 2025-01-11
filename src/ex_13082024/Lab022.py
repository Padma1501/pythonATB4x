# Take a user inputs a,b and calculate the sum, mul, sub, div

"""
num1 = input("Enter the num1")
num2 = input("Enter the num2")

#89+89 = 178 but it give 8989
Because it was a string 89+89 it can concatinate, they will join together

so we can convert string to integer
str -> int
"""
num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))

print(type(num1))
print(type(num2))

print("sum is ", num1+num2)
print("sub is ", num1-num2)
print("mul is ", num1*num2)
print("div is ", num1/num2)  # 1.0 output bcoz python is smrt language- 3/4 = 1.5
# in java this options is removed but in python it will prints
# 3/2 = 1.5 whenever we divide there are high no of chances the float wil come ***

