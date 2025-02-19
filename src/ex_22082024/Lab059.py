###  Match statemnt - used in python only
# switch statement - java
# match the o/p and execute
# works in python only > 3.10


"""
Syntax for match

match variable:
    case pattern1:
        # code block
    case pattern2:
        # code block

"""


# write a program to ask the user which browser he want to run automation

browser_name = input("Enter the name of the browser \n")
browser_name = browser_name.lower()
match browser_name:
    case "Firefox":
        print("Execute the firefox code")
    case "Chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "Mozilla":
        print("Execute the Mozilla code")
    case __:
        print("Browser not found")

        # case is a keyword - match with the case
