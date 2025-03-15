# Functions with arguements, parameters


def greet():
    print(" Hello")


def greet_by_name(name): # name -> variable name
    print("Hello", name)
greet_by_name("padma")
greet_by_name(123)
greet_by_name("abc123")
greet_by_name("true")
greet_by_name('false')


result = greet_by_name('false')
print(result) # return type gives none