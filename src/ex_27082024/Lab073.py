# Pizza lovers - Yes

def make_pizza(*toppings):
    for topin in toppings:
        print(topin)

print(" program started")
pramod = make_pizza("tomato")
dhhir = make_pizza("Olives", "mushroom", "paneer")
vinay = make_pizza("mushroom", "pineapple", "paneer", "sweetcorn")
print(" program end")

# Builtin also used * (max func)
r = max(1, 2, 3, 4, 8)
print(r)