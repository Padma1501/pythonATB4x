def print_arguements(*args):
    #*args = multiple arguements with no limit , -> list
    #print(args[0])
    for i in args:
        print(i)

# list = [ " padma", " panda" ]


print_arguements("padma", "Trees", "nature")
print_arguements("padma", "Trees")
print_arguements("padma")
print_arguements("padma", 10)
print_arguements("padma", "PANDA")
#print_arguements()- minimum 1 arguement is important



print("padma", "panda", True, False,)