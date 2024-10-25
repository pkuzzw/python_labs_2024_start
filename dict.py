import json
# Reading the JSON file
with open('students.json', 'r') as file:
    data = json.load(file)

# Accessing the list of students
students = data["students"]
print(students)

# Iterating through the list of students
for student in students:
    print(student)

# Accessing individual student data
for student in students:
    student_id = student["id"]
    student_name = student["name"]
    student_age = student["age"]
    student_grades = student["grades"]
    
    print(f"ID: {student_id}, Name: {student_name}, Age: {student_age}, Grades: {student_grades}")


# Accessing nested data (grades)
for student in students:
    student_name = student["name"]
    math_grade = student["grades"]["math"]
    science_grade = student["grades"]["science"]
    
    print(f"Name: {student_name}, Math Grade: {math_grade}, Science Grade: {science_grade}")
    