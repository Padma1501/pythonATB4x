### TASK 7

# lEAP YEAR CHECKER:
#Create a program that determines whetherr a give year is a leap year
# A leap year is divisuble by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.


# found leap year condition - check browser


# Leap Year Checker

year = int(input("Enter the year\n"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Lear Year")