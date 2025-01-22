### Task #3


#
# - Explain the difference between the = operator and the == operator in Python.
#
# - What does the ** operator do in Python, and how is it used?
#
# - What does the ^ operator do in Python, and in what context is it commonly used?



"""
= -> Its a assignment operator 
-> which is used to store the right value to the left value ref
== -> compasrison operator
-> Used to compare the two values are same or not 
-> True or False


"""

age = 60
print(age)

print(2 == 2)
print(2 == 3)

"""
- ** operator -> power 
-> in python, we used ** operator for calculating the power 
-> it is used as 2**3

"""
print(2**3)

"""
^ operator-> XOR- Exclusive OR operator """
# In Python, the ^ operator is the bitwise XOR (exclusive OR) operator.
#
# The ^ operator compares each bit of two integers. For each bit position:
# The result bit is 1 if the corresponding bits of the operands are different
# (one is 1 and the other is 0).
# The result bit is 0 if the corresponding bits are the same (both 0 or both 1).
a = 10   # binary: 1100
b = 8   # binary: 0111
result = a ^ b  # binary: 1011, which is 11 in decimal
print(result)   # Output: 11
