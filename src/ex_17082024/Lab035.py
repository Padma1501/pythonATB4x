# TASK #4
#  write a python program to calculate the
# area of a circle given its radius using the formula
#  '''area=π*r^2''' (Take pie as 3.14 )
import math

#  Logic building formula

#  step 1 - figure out the inputs and output
#  input -> r -> what is the data type of this -> float ( we are asking the person who is giving this )
#  pi = 3.14 -> ask which one we use math or some other
#  power -> ask which one we use like pow func or ** -> said any

# o/p -> float - area, print area


#  step 2
#  rough logic -> area = 3.14*pow(r,2)

# step 3

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
#  reformate the code above thats why we are using formating
#  formated_number = f"{number: .2f}

#  what is diff b/w * and **
#  * is a multiplication
# ** -> pow
