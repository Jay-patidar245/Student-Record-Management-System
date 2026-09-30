from student import Student
from storage import load_students, save_students


class StudentManager:
    """Handles student records and CRUD-style operations."""

    def __init__(self):
        self.students = load_students()

    def add_student(self, student):
        if self.find_by_id(student.student_id):
            return False
        self.students.append(student)
        save_students(self.students)
        return True

    def find_by_id(self, student_id):
        student_id = str(student_id).strip()
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search(self, keyword):
        keyword = keyword.lower().strip()
        return [
            student for student in self.students
            if keyword in student.student_id.lower()
            or keyword in student.name.lower()
        ]

    def update_marks(self, student_id, marks):
        student = self.find_by_id(student_id)
        if not student:
            return False
        student.marks.update({subject: float(score) for subject, score in marks.items()})
        save_students(self.students)
        return True

    def delete_student(self, student_id):
        student = self.find_by_id(student_id)
        if not student:
            return False
        self.students.remove(student)
        save_students(self.students)
        return True

    def all_students(self):
        return list(self.students)
