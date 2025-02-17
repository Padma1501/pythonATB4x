# conditions and loops


# Write a program to take a user age and let him know if he can go the club
#21

# Logic building
# 1. user input - data type - int
# o/p ->  String -> User if he can go or not

# 2. Rough logic
# age > 21 -> print can go
# age < 21 -> print can't go

# 3. Write the logic
age = input(" Enter your age\n")
age= int(age)

if age > 21:
    print(f"Can go club -> {age}")
else:
    print(f"Can't go with this age -> {age} ")

# f is string formatting we use
