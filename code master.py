# Sample list of students with first name, last name, and student number
students = [
     {"first_name": "Amirali", "last_name": "gholami", "student_number":8077},
     {"first_name": "taher", "last_name": "jamali", "student_number": 8104},
     {"first_name": "Reza", "last_name": "paktinat", "student_number":8113},
     {"first_name": "arvin", "last_name": "hatef", "student_number": 8102},
       {"first_name": "Maryam", "last_name": "Gholipour", "student_number": 8210},
     {"first_name": "Parnia", "last_name": "Nouri", "student_number": 8189},
       {"first_name": "Yasaman", "last_name": "Kazemi", "student_number": 8009},
     {"first_name": "Sarah", "last_name": "RokniDoost", "student_number": 8004},
    
    
]

# Function to display students
def display_students(sorted_list, criteria):
    print(f"\nStudents sorted by {criteria}:")
    for student in sorted_list:
        print(f"First Name: {student['first_name']}, Last Name: {student['last_name']}, Student Number: {student['student_number']}")

# Sort by first name
sorted_by_first_name = sorted(students, key=lambda x: x["first_name"])
display_students(sorted_by_first_name, "First Name")

# Sort by last name
sorted_by_last_name = sorted(students, key=lambda x: x["last_name"])
display_students(sorted_by_last_name, "Last Name")

# Sort by student number
sorted_by_student_number = sorted(students, key=lambda x: x["student_number"])
display_students(sorted_by_student_number, "Student Number")