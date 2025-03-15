"""
User defined - function
1. they cant return -> none return
2. they can return something
They have parameters
They dont parameters / arguemnets

"""


# 1. they cant return -> none return
# no return type and no parameter / arguement - NRNP
def greet():  # ()- no parameters are there so give none
    print("Hello")

result = greet()
print(result)


# 2. No return type with arguements
def greet_by_name(name):
    print("Hello", name)
greet_by_name("padma")


# 3. No return type and with default arguement
def say_hello_default_arg(name="padmaaaaa"):
    print("hello", name)

#say_hello_default_arg("Panda") # def arg -> default arguement
say_hello_default_arg()
say_hello_default_arg(name = "kanna") # positional arguement




def multiple_args(name1="Arpita", name2="pramod", name3="Amit"):
    print("multiple arguements", name1, name2, name3)

multiple_args(name1="priya", name2="yunus", name3="Deepu")
multiple_args(name1="PRAMOD")


# 4. Arguement + return type
def sum_of_two_number(num1,num2):
    return num1+num2

def sum_of_two_number_with_default(num1=100,num2=200):
    return num1+num2


# result = sum_of_two_number(10,34)
result = sum_of_two_number(num1=10, num2=34)
result = sum_of_two_number_with_default()
print(result)


def greet_by_name(padma):  # name -> variable name, arguemnts / parameters
    print("Hello", padma.upper())

greet_by_name("padma")
greet_by_name('123')
greet_by_name('True')
greet_by_name("false")
