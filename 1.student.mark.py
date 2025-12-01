students = []
courses = []
marks = []

def input_numbers_of_students():
    count = int(input("Enter number of students: "))
    return count
def input_student_information():
    print("\n---Enter student information---")
    id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    student = {"id": id, "name": name, "dob": dob}
    students.append(student)
def input_number_of_courses():
    count = int(input("Enter number of courses: "))
    return count
def input_course_information():
    print("\n---Enter course information---")
    id = int(input("Enter course ID: "))
    name = input("Enter course name: ")
    course = {"id": id, "name": name}
    courses.append(course)
def input_marks():
    print("enter marks: ")
    if len(courses) == 0:
        print("No courses entered. Please add courses first")
        return
    print("select a course by ID:")
    for c in courses:
        print(f"ID: {c['id']} - {c['name']}")
    selected_course_id = int(input("Enter course ID to input marks: "))
    print(f"Entering marks for course {selected_course_id}")
    for s in students:
        mark = float(input(f"Enter mark for student {s['name']} (ID: {s['id']}): "))
        # luu diem:
        data = {
            'course_id': selected_course_id,
            'student_id': s['id'],
            'mark': mark
        }
        marks.append(data)
def list_student():
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")
def list_course():
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
def show_marks():
    print("\n--- Marks List ---")
    course_id = int(input("Enter course ID: "))
    print(f"Mark for course: {course_id}")
    for m in marks:
        if m['course_id'] == course_id:
            student_name = ""
            for s in students:
                if s['id'] == m['student_id']:
                    student_name = s['name']
                    break
            print(f"Student: {student_name} (ID: {m['mark']}) - Mark: {m['mark']}")
#
#
# Main
if __name__ == "__main__":
    num_students = input_numbers_of_students()
    for _ in range (num_students):
        input_student_information()

    num_courses = input_number_of_courses()
    for _ in range (num_courses):
        input_course_information()

    while True:
        print("\n--- Main Menu ---")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Show marks for a course")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_student()
        elif choice == 2:
            list_course()
        elif choice == 3:
            input_marks()
        elif choice == 4:
            show_marks()
        elif choice == 5:
            print("Exiting program ..")
            break
        else:
            print("Please enter a valid choice")
