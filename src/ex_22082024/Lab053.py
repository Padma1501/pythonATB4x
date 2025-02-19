for i in range(0, 100):
    print(i)

for i in range(0, 10):
    print(i)
    if i == 5:
        break


# Logic
"""
| i |  condition | o/p
| 0 | 0==5 -> false | o/p = 0
| 0 | 1==5 -> false | o/p = 1
| 0 | 2==5 -> false | o/p = 2
| 0 | 3==5 -> false | o/p = 3
| 0 | 4==5 -> false | o/p = 4
| 0 |5==5 -> true -> breako/p = 5

ifcondition is true it breaks and it doesnt print anything

"""