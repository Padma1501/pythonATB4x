# STRING
name = "padma"
print(name)
print(type(name))
print(name.upper())
print(name.lower())
print(len(name)) # length starts from 1



age = "90"  # which is something in ""- it is string
print(type(age))
age = 90
print(type(age))

name = "This is big line"
print(type(name))
#name = name + 1 # its not printed bcoz of only strings can concatinate
#concatinate - combine strings
# then we use as name + "1"or str(1) then its combine

name = name + "1"
#name = name + str(1)
print(name)


"""
CONCATINATION
"""
first_name = "padma"
last_name = "kuppela"
full_name = first_name+last_name
print(full_name)

how_many_planes_i_have = None  # Nonetype ( none is one of type )
print(how_many_planes_i_have)
print(type(how_many_planes_i_have))
#null is not present in python it present in java

val = 0 # this is a int not none

"""
ID - it is a function 
"""
#id
age = 10
print(id(age))  #140723919850200- address of object
age2 = 10
print(id(age2)) #140723919850200- same address is located bcoz 10 is stored in age again we give input as 10 the value same thats why it gives same address
age3 = 12
print(id(age3))# 140723919850264 - the id will change


