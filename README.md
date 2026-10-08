# Student Attendance Management System

A mini project for managing student attendance in educational institutions. The system allows administrators to add students, mark attendance for a selected date, and view reports.

## Features
- Add and manage student records
- Record attendance for each student by date
- Mark attendance as Present, Absent, or Late
- View student attendance summaries
- Dashboard with quick statistics
- Simple SQLite database backend
- Responsive web interface

## Tech Stack
- Python 3
- Flask
- SQLite3
- HTML5 + CSS3 + JavaScript

## Project Structure

```text
student-attendance-management/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── data/
│   └── attendance.db
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── students.html
│   ├── attendance.html
│   └── reports.html
└── docs/
    └── PROJECT_DOCUMENTATION.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rakeshkolukulapalli-ops/student-attendance-management.git
   cd student-attendance-management
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

```bash
python app.py
```

Then open the browser at:
```text
http://127.0.0.1:5000/
```

## How It Works

### Add Students
- Go to the Students page.
- Fill in the student's name, roll number, department, year, and phone number.
- Click Save Student.

### Mark Attendance
- Go to the Attendance page.
- Select a date.
- Choose the status for each student.
- Submit the attendance list.

### View Reports
- Go to the Reports page.
- Check the attendance summary for all students.

## Database Design

The app uses SQLite with two tables:

1. students
   - id
   - name
   - roll_no
   - department
   - year
   - phone
   - created_at

2. attendance
   - id
   - student_id
   - attendance_date
   - status
   - notes
   - created_at

## Screenshots

The project includes a responsive dashboard and forms for attendance management.

## Future Enhancements
- Login and role-based access
- Admin-only editing and deletion
- Export attendance to Excel/CSV
- Monthly attendance analytics
- Email or SMS notifications

## License
This project is provided for educational use and demonstration purposes.

## Author
Student mini project
