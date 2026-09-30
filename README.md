# Student Record Management System

## 1. Project Title
Student Record Management System

## 2. Overview
A Python-based menu-driven application for maintaining student academic records. It allows the user to add, search, update, calculate results, display records, and delete records.

## 3. Main Features
- Add student with subject marks
- Search student by ID or name
- Update marks
- Calculate total and percentage
- Display pass/fail result
- Display all students
- Delete a student record
- Save records in a JSON file

## 4. Technologies Used
- Python 3
- JSON for local data storage
- Git/GitHub for version control

No external Python package is required.

## 5. Project Structure
```text
Student_Record_Management_System/
│
├── main.py
├── student.py
├── student_manager.py
├── storage.py
├── validators.py
├── reports.py
├── students.json
├── statement.md
├── README.md
└── tests/
    └── test_student_manager.py
```

## 6. How to Run

### Step 1: Install Python
Install Python 3 from the official Python website if it is not already installed.

### Step 2: Open the project folder
Open a terminal/command prompt inside this project folder.

### Step 3: Run the application
```bash
python main.py
```

If your computer uses `python3`, use:
```bash
python3 main.py
```

### Step 4: Use the menu
Choose options 1-7 and follow the prompts.

## 7. Data Storage
Student records are automatically saved in `students.json` in the project folder.

## 8. Testing
If pytest is available:
```bash
pytest
```

The tests check total calculation, percentage calculation, and pass/fail result logic.

## 9. Notes
This project is designed for academic demonstration. Before submission, the student should run it, understand each module, add their own screenshots, and personalize the documentation where appropriate.
