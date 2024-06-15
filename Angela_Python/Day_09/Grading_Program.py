student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Covert scores into grades.
for i in student_scores:
    score = student_scores[i]
    if score > 90:
        student_grades[i] = "Outstanding"
    elif score > 80:
        student_grades[i] = "Exceeds Expectations"
    elif score > 70:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"

print(student_grades)
print(student_scores)