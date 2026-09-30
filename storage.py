import json
from pathlib import Path
from student import Student

DATA_FILE = Path(__file__).resolve().parent / "students.json"


def load_students():
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return [Student.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Warning: students.json is invalid. Starting with an empty record.")
        return []


def save_students(students):
    data = [student.to_dict() for student in students]
    DATA_FILE.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )
