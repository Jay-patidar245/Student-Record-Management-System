from student import Student
from student_manager import StudentManager
from validators import get_non_empty, get_mark, get_choice
from reports import print_student, print_student_list

SUBJECTS = ["Python", "Maths", "English", "EVS"]


def add_student(manager):
    print("\n--- Add Student ---")
    student_id = get_non_empty("Enter student ID: ")
    if manager.find_by_id(student_id):
        print("A student with this ID already exists.")
        return

    name = get_non_empty("Enter student name: ")
    course = get_non_empty("Enter course: ")

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_mark(f"Enter marks in {subject} (0-100): ")

    student = Student(student_id, name, course, marks)
    manager.add_student(student)
    print("Student added successfully.")


def search_student(manager):
    print("\n--- Search Student ---")
    keyword = get_non_empty("Enter student ID or name: ")
    results = manager.search(keyword)

    if len(results) == 1:
        print_student(results[0])
    else:
        print_student_list(results)


def update_marks(manager):
    print("\n--- Update Marks ---")
    student_id = get_non_empty("Enter student ID: ")
    student = manager.find_by_id(student_id)

    if not student:
        print("Student not found.")
        return

    print("Enter new marks:")
    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_mark(f"{subject}: ")

    manager.update_marks(student_id, marks)
    print("Marks updated successfully.")
    print_student(manager.find_by_id(student_id))


def display_result(manager):
    print("\n--- Calculate Total / Percentage / Result ---")
    student_id = get_non_empty("Enter student ID: ")
    student = manager.find_by_id(student_id)

    if student:
        print_student(student)
    else:
        print("Student not found.")


def delete_student(manager):
    print("\n--- Delete Student ---")
    student_id = get_non_empty("Enter student ID: ")

    if manager.delete_student(student_id):
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n" + "=" * 55)
        print("       STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 55)
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Marks")
        print("4. Calculate Total & Percentage")
        print("5. Display All Students")
        print("6. Delete Student")
        print("7. Exit")
        print("=" * 55)

        choice = get_choice("Enter your choice (1-7): ", 1, 7)

        if choice == 1:
            add_student(manager)
        elif choice == 2:
            search_student(manager)
        elif choice == 3:
            update_marks(manager)
        elif choice == 4:
            display_result(manager)
        elif choice == 5:
            print_student_list(manager.all_students())
        elif choice == 6:
            delete_student(manager)
        else:
            print("Thank you for using the system.")
            break


if __name__ == "__main__":
    main()
