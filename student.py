class Student:
    """Represents one student's academic record."""

    def __init__(self, student_id, name, course, marks):
        self.student_id = str(student_id)
        self.name = name
        self.course = course
        self.marks = {subject: float(score) for subject, score in marks.items()}

    def total(self):
        return sum(self.marks.values())

    def percentage(self):
        if not self.marks:
            return 0.0
        return self.total() / len(self.marks)

    def result(self):
        if not self.marks:
            return "N/A"
        return "PASS" if all(score >= 40 for score in self.marks.values()) else "FAIL"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "course": self.course,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["course"],
            data.get("marks", {})
        )
