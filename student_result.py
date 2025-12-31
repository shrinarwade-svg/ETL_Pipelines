# student_result.py

def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    return total, percentage, grade


student_marks = [80, 75, 70, 65, 85]

total, percent, grade = calculate_result(student_marks)

print("Total Marks:", total)
print("Percentage:", percent)
print("Grade:", grade)
