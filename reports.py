def print_student(student):
    print("\n" + "=" * 55)
    print("STUDENT RESULT")
    print("=" * 55)
    print(f"ID         : {student.student_id}")
    print(f"Name       : {student.name}")
    print(f"Course     : {student.course}")
    print("-" * 55)
    for subject, score in student.marks.items():
        print(f"{subject:<25} {score:>7.2f}")
    print("-" * 55)
    print(f"Total      : {student.total():.2f}")
    print(f"Percentage : {student.percentage():.2f}%")
    print(f"Result     : {student.result()}")
    print("=" * 55)


def print_student_list(students):
    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 78)
    print(f"{'ID':<12}{'Name':<22}{'Course':<18}{'Percentage':<12}{'Result'}")
    print("=" * 78)
    for student in students:
        print(
            f"{student.student_id:<12}"
            f"{student.name[:20]:<22}"
            f"{student.course[:16]:<18}"
            f"{student.percentage():<12.2f}"
            f"{student.result()}"
        )
    print("=" * 78)
