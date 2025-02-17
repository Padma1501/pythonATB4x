# Problem to find the max between two


# Logic building formula


# 1. User inputs -> Two integers
# 2. o/p -> int 1 which ever is greater max num it will return
# 3. - input method
# we need to ask the interviewer what is the data type looking for

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
if num1 > num2:
    print("Max is num1")
else:
    print("Max is num2")
    print(f"Max is {num2}")
