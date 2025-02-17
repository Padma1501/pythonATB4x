# Grade calculator ----most imp in interview

# Write a program that calculates and diplays the letter grade for a given numerical score
# e.g A , B, C, D, F
# based on the following scale

# A: 9.-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter your score\n"))
grade = "F"
# score >=90 and score <=100 -> "A"
# Score >=80 and scotr <=89 -> "B"

if score >= 90 and score <= 100:  # 90 <= score <= 100: - simplified chain comparison
    grade = "A"
    print("Your grade is", grade)
elif score >= 80 and score < 90:
    grade = "B"   # print("Your grade is", "B")
    print("Your grade is", grade)
elif score >= 70 and score < 80:
    grade = "C"
    print("Your grade is", grade)
elif score >= 60 and score < 70:
    grade = "D"
    print("Your grade is", grade)
elif score >= 100:
    print("You are superwomen")
else:
    grade = "F"
    print("Your grade is", grade)
