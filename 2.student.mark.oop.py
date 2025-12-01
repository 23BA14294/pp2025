class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""

    def input(self):
        self.__id = input("Enter Student ID: ")
        self.__name = input("Enter Student Name: ")
        self.__dob = input("Enter Student DoB: ")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}"

class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""

    def input(self):
        self.__id = input("Enter Course ID: ")
        self.__name = input("Enter Course Name: ")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}"

class MarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        num = int(input("Enter number of students: "))
        for _ in range(num):
            s = Student()
            s.input()
            self.students.append(s)

    def input_courses(self):
        num = int(input("Enter number of courses: "))
        for _ in range(num):
            c = Course()
            c.input()
            self.courses.append(c)

    def list_students(self):
        print("\n--- Student List ---")
        for s in self.students:
            print(s)

    def list_courses(self):
        print("\n--- Course List ---")
        for c in self.courses:
            print(c)

    def input_marks(self):
        if not self.courses:
            print("No courses available.")
            return

        self.list_courses()
        course_id = input("Select Course ID to input marks: ")

        if course_id not in [c.get_id() for c in self.courses]:
            print("Course not found.")
            return

        if course_id not in self.marks:
            self.marks[course_id] = {}

        print(f"Entering marks for course {course_id}:")
        for s in self.students:
            mark = float(input(f"Enter mark for {s.get_name()} (ID: {s.get_id()}): "))
            self.marks[course_id][s.get_id()] = mark

    def show_marks(self):
        course_id = input("Enter Course ID to view marks: ")
        if course_id in self.marks:
            print(f"Marks for Course: {course_id}")
            for s in self.students:
                if s.get_id() in self.marks[course_id]:
                    print(f"Student: {s.get_name()} - Mark: {self.marks[course_id][s.get_id()]}")
        else:
            print("No marks found for this course.")


#
#
# Main
if __name__ == "__main__":
    system = MarkManagement()

    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM  ---")
        print("1.Input Students")
        print("2.Input Courses")
        print("3.List Students")
        print("4.List Courses")
        print("5.Input Marks")
        print("6.Show Marks")
        print("7.Exit")

        choice = input("Your choice: ")

        if choice == '1':
            system.input_students()
        elif choice == '2':
            system.input_courses()
        elif choice == '3':
            system.list_students()
        elif choice == '4':
            system.list_courses()
        elif choice == '5':
            system.input_marks()
        elif choice == '6':
            system.show_marks()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice")