# WHAT IS ESCAPE SEQUENCE ?

print("HELLOW", "world")
print("HELLOW/nworld") # /n -> newline
print("HELLOW/tworld") # /n -> tabline
print("HELLO/bWworld") # /n -> backspace


# dir = 'c:/padma/n.txt'
# dir = "c:/padma/n.txt" both are not printed if we use single quote or double quotes
# where this r concept  will be used ?
# Automation API, web automation, file_path -> r concept -> raw
dir = r"c:/padma/n.txt"
dir2 = r'c:/padma/n.txt'
print(dir)
print(dir2)

name = 'padma/padhu' #-> whenever we use single quote then we add extra slash
name2 = "padma" "padhu"

print(name)
print(name2)
