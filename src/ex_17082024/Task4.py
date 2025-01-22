### Task #4



# - Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

import math

radius = float(input("Enter the radius of the circle\n"))
#  press and hold alt key, type 092 then backslash will print
math.pi = 3.14
print(radius)
print(math.pi)
area = math.pi * math.pow(radius, 2) # __y ignore this
area2 = 3.14 * (radius**2)
print("Area of the circle is ", area)
print("Area of the circle is ", area2)
print(f"Area of the circle is ->{area: .2f}" )