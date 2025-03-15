### TASK 9
# Triangle classifier


#Writs a program that classifies a triangle based on its side lenghs.
# #Given three inout values representing the lengths of the
# sides:
# Determine if the triangle is equilateral ( all sides are equal ),
# isosceles ( exactly two sides are equal ), or scalene (no sides are equal ).
# Use an if-else statement to cleassify the triangle.

# browse for detailed pictures


a = float(input("Enter the side a: "))
b = float(input("Enter the side b: "))
c = float(input("Enter the side c: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


