physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
biology = float(input("Enter Biology marks: "))
math = float(input("Enter Mathematics marks: "))
computer = float(input("Enter Computer marks: "))

total = physics + chemistry + biology + math + computer
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
