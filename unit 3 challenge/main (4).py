class Student:
    def __init__(self, name, roll_no, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list,
                             key=lambda student: student.cgpa,
                             reverse=True)
    return sorted_students

students = [
    Student("jojo", "C169", 8.8),
    Student("dio", "A269", 8.6),
    Student("jodio", "B369", 9.3),
    Student("ff", "F469", 7.2),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print("Name: {}, Roll No: {}, CGPA: {}".format(student.name, student.roll_no, student.cgpa))
