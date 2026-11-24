# Student Grade Manager

## Project Discussion, Setup Guide, Testing, and Code Explanation

## 1. Project overview

The **Student Grade Manager** is a terminal-based Python application. It allows a user to:

- Add any number of students.
- Enter a mark from 0 to 100.
- Automatically calculate a grade from A to E.
- Display all student records in an aligned table.
- Calculate the class average.
- Show the highest and lowest marks.
- Handle invalid input without crashing.
- Keep running until the user chooses **Quit**.

The project is stored in one file:

```text
grade_manager.py
```

No external Python packages are required.

---

## 2. Grading scale

| Mark range | Grade |
|---:|:---:|
| 90 to 100 | A |
| 80 to below 90 | B |
| 70 to below 80 | C |
| 60 to below 70 | D |
| Below 60 | E |

The boundaries are inclusive. For example, exactly `90` is an A and exactly `80` is a B.

---

## 3. Complete Python code

Save the following code in a file named `grade_manager.py`:

```python
"""Student Grade Manager.

Run with:
    python grade_manager.py
"""


def get_grade(mark):
    """Return the letter grade for a validated mark from 0 to 100."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


def get_valid_name():
    """Prompt until the user enters a non-empty student name."""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def get_valid_mark():
    """Prompt until the user enters a numeric mark between 0 and 100."""
    while True:
        raw_mark = input("Enter mark (0-100): ").strip()

        if not raw_mark:
            print("Mark cannot be empty. Please enter a number from 0 to 100.")
            continue

        try:
            mark = float(raw_mark)
        except ValueError:
            print("Invalid mark. Please enter a number from 0 to 100.")
            continue

        if not 0 <= mark <= 100:
            print("Mark must be between 0 and 100.")
            continue

        return mark


def format_mark(mark):
    """Display whole-number marks without a decimal point."""
    if mark.is_integer():
        return str(int(mark))
    return f"{mark:.2f}".rstrip("0").rstrip(".")


def add_student(students):
    """Read, validate, and store one student record."""
    name = get_valid_name()
    mark = get_valid_mark()

    students.append(
        {
            "name": name,
            "mark": mark,
            "grade": get_grade(mark),
        }
    )

    print(f"Added {name} successfully.\n")


def show_results(students):
    """Print an aligned results table and class statistics."""
    if not students:
        print("No students have been added yet.\n")
        return

    name_width = max(12, max(len(student["name"]) for student in students) + 2)

    print()
    print(f'{"Name":<{name_width}} {"Mark":>7}   {"Grade":>5}')
    print("-" * (name_width + 16))

    for student in students:
        mark_text = format_mark(student["mark"])
        print(
            f'{student["name"]:<{name_width}} '
            f'{mark_text:>7}   '
            f'{student["grade"]:>5}'
        )

    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)

    print("-" * (name_width + 16))
    print(
        f"Average: {average:.1f}    "
        f"Highest: {format_mark(max(marks))}    "
        f"Lowest: {format_mark(min(marks))}\n"
    )


def show_menu():
    """Display the application menu."""
    print("Student Grade Manager")
    print("1. Add student")
    print("2. Show results")
    print("3. Quit")


def main():
    """Run the menu loop without crashing on invalid input."""
    students = []  # A list allows different students to have the same name.

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip().lower()

        if choice in {"1", "add", "a"}:
            add_student(students)
        elif choice in {"2", "show", "s"}:
            show_results(students)
        elif choice in {"3", "quit", "q", "exit"}:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
```

---

## 4. How the program works

### 4.1 Program entry point

The last two lines are:

```python
if __name__ == "__main__":
    main()
```

When `python grade_manager.py` is run, Python calls `main()`. The `main()` function creates an empty student list and starts the menu loop.

---

### 4.2 Student storage

Inside `main()`, the program creates:

```python
students = []
```

This is a Python list. Each student is stored as a dictionary:

```python
{
    "name": "Priya",
    "mark": 92.0,
    "grade": "A"
}
```

After adding several students, the data has this general structure:

```python
[
    {"name": "Priya", "mark": 92.0, "grade": "A"},
    {"name": "Arun", "mark": 78.0, "grade": "C"},
    {"name": "Divya", "mark": 59.0, "grade": "E"}
]
```

A list was chosen because:

- It preserves the order in which students are added.
- It allows multiple students with the same name.
- It is simple to loop through when printing the results.
- It makes calculating statistics straightforward.

---

### 4.3 Grade calculation with `get_grade()`

```python
def get_grade(mark):
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"
```

The conditions are checked from the highest grade downward.

Examples:

- `get_grade(92)` returns `"A"`.
- `get_grade(80)` returns `"B"`.
- `get_grade(78)` returns `"C"`.
- `get_grade(60)` returns `"D"`.
- `get_grade(59)` returns `"E"`.

Checking from the highest boundary downward means no upper limit is needed in each condition after the mark has already been validated.

---

### 4.4 Name validation with `get_valid_name()`

```python
def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")
```

The function:

1. Requests a student name.
2. Uses `.strip()` to remove spaces from the beginning and end.
3. Returns the name if it is not empty.
4. Displays an error and repeats if the input is empty.

The `while True` loop continues until valid input is supplied.

---

### 4.5 Mark validation with `get_valid_mark()`

The mark validation handles several error cases.

#### Empty input

```python
if not raw_mark:
    print("Mark cannot be empty. Please enter a number from 0 to 100.")
    continue
```

Pressing Enter without typing a mark is rejected.

#### Non-numeric input

```python
try:
    mark = float(raw_mark)
except ValueError:
    print("Invalid mark. Please enter a number from 0 to 100.")
    continue
```

Text such as `abc` cannot be converted to a number. The `ValueError` is caught, so the program does not crash.

#### Out-of-range input

```python
if not 0 <= mark <= 100:
    print("Mark must be between 0 and 100.")
    continue
```

Values below 0 or above 100 are rejected.

Examples:

- `-25` is rejected.
- `150` is rejected.
- `105` is rejected.
- `0` is accepted.
- `100` is accepted.

#### Decimal input

The program uses:

```python
mark = float(raw_mark)
```

Therefore, valid decimal marks are accepted.

For example:

```text
.25
```

is converted by Python to:

```text
0.25
```

Because `0.25` is between 0 and 100, the program accepts it and assigns grade E. This is valid behavior, not an error.

---

### 4.6 Adding a student

```python
def add_student(students):
    name = get_valid_name()
    mark = get_valid_mark()

    students.append(
        {
            "name": name,
            "mark": mark,
            "grade": get_grade(mark),
        }
    )
```

The function:

1. Gets a valid name.
2. Gets a valid mark.
3. Calculates the grade.
4. Builds a dictionary.
5. Appends the dictionary to the `students` list.

For the input `MANI` and `65`, the stored record is:

```python
{"name": "MANI", "mark": 65.0, "grade": "D"}
```

---

### 4.7 Formatting marks

```python
def format_mark(mark):
    if mark.is_integer():
        return str(int(mark))
    return f"{mark:.2f}".rstrip("0").rstrip(".")
```

Marks are stored as floating-point numbers. This function improves their display:

- `80.0` is displayed as `80`.
- `65.0` is displayed as `65`.
- `78.5` is displayed as `78.5`.
- `0.25` is displayed as `0.25`.

The formatting does not change the stored value. It only changes how it appears in the results table.

---

### 4.8 Showing results

If the user chooses option 2 before adding any students, this check prevents an error:

```python
if not students:
    print("No students have been added yet.\n")
    return
```

Without this check, operations such as `max([])` and `min([])` would fail on an empty list.

For existing students, the function calculates a suitable name-column width:

```python
name_width = max(12, max(len(student["name"]) for student in students) + 2)
```

This keeps the table aligned even when a student has a longer name.

---

### 4.9 Class statistics

The program creates a list containing only the marks:

```python
marks = [student["mark"] for student in students]
```

It then calculates:

```python
average = sum(marks) / len(marks)
max(marks)
min(marks)
```

- `sum(marks) / len(marks)` calculates the average.
- `max(marks)` finds the highest mark.
- `min(marks)` finds the lowest mark.

The average is displayed to one decimal place using:

```python
f"{average:.1f}"
```

---

### 4.10 Menu loop

The main loop is:

```python
while True:
    show_menu()
    choice = input("Choose an option (1-3): ").strip().lower()
```

The program accepts both menu numbers and selected text shortcuts:

- `1`, `add`, or `a` adds a student.
- `2`, `show`, or `s` shows results.
- `3`, `quit`, `q`, or `exit` closes the program.

Any other entry produces:

```text
Invalid choice. Enter 1, 2, or 3.
```

The `break` statement exits the loop when Quit is selected.

---

## 5. Running the project on Windows

### 5.1 Save the file

Save `grade_manager.py` in:

```text
F:\.SocialEagal\Day2\
```

The complete path should be:

```text
F:\.SocialEagal\Day2\grade_manager.py
```

Make sure Windows has not saved it as:

```text
grade_manager.py.txt
```

### 5.2 Open the project folder in Visual Studio Code

1. Open Visual Studio Code.
2. Select **File > Open Folder**.
3. Open `F:\.SocialEagal\Day2`.
4. Open `grade_manager.py` from the Explorer panel.

### 5.3 Run from PowerShell or the VS Code terminal

```powershell
cd "F:\.SocialEagal\Day2"
dir
python .\grade_manager.py
```

The `dir` command should list `grade_manager.py` before the Python command is run.

Expected menu:

```text
Student Grade Manager
1. Add student
2. Show results
3. Quit
Choose an option (1-3):
```

---

## 6. Troubleshooting discussion

### 6.1 `SyntaxError` after typing `Download grade_manager.py`

The command was entered at the Python prompt:

```text
>>>
```

`Download grade_manager.py` is not Python code, so Python reported a `SyntaxError`.

To leave the Python interpreter:

```python
exit()
```

Then run the file from Command Prompt or PowerShell:

```powershell
python grade_manager.py
```

Key difference:

- `F:\.SocialEagal\Day2>` is a Windows command prompt.
- `PS F:\.SocialEagal\Day2>` is a PowerShell prompt.
- `>>>` is the interactive Python interpreter.

The script command belongs in Command Prompt or PowerShell, not at `>>>`.

### 6.2 `[Errno 2] No such file or directory`

This error means Python is installed and running, but `grade_manager.py` cannot be found in the current directory.

Use:

```powershell
dir
```

If `grade_manager.py` is missing, save or move it into the current folder. Then run:

```powershell
python .\grade_manager.py
```

### 6.3 `[Errno 22] Invalid argument`

The Visual Studio Code terminal attempted to run a path similar to:

```text
f:/.SocialEagal/Day2/Download grade_manager.py
```

The problem was the incorrect filename or path. The project file must be called exactly:

```text
grade_manager.py
```

The reliable approach is:

```powershell
cd "F:\.SocialEagal\Day2"
python .\grade_manager.py
```

This avoids running the project from the Visual Studio Code installation directory.

---

## 7. Testing performed

The following values were tested:

- Negative mark: `-25`
- Above-maximum mark: `150`
- Decimal mark: `.25`
- Valid marks: `80`, `65`, `15`, and `45`
- Duplicate decimal mark: `0.25`

Observed validation:

```text
Enter mark (0-100): -25
Mark must be between 0 and 100.

Enter mark (0-100): 150
Mark must be between 0 and 100.

Enter mark (0-100): .25
Added error2 successfully.
```

The first two values were correctly rejected. The `.25` value was correctly interpreted as `0.25` and accepted.

The resulting records were:

| Name | Mark | Grade |
|---|---:|:---:|
| GPN | 80 | B |
| MANI | 65 | D |
| Raja | 15 | E |
| Ramesh | 45 | E |
| Error | 0.25 | E |
| error2 | 0.25 | E |

### Statistics verification

Marks:

```text
80, 65, 15, 45, 0.25, 0.25
```

Sum:

```text
80 + 65 + 15 + 45 + 0.25 + 0.25 = 205.5
```

Number of students:

```text
6
```

Average:

```text
205.5 / 6 = 34.25
```

The program displays the average to one decimal place:

```text
Average: 34.2
```

Python's standard floating-point formatting produces `34.2` for this value. The other statistics are:

```text
Highest: 80
Lowest: 0.25
```

---

## 8. Example complete run

```text
Student Grade Manager
1. Add student
2. Show results
3. Quit
Choose an option (1-3): 1
Enter student name: Priya
Enter mark (0-100): 92
Added Priya successfully.

Student Grade Manager
1. Add student
2. Show results
3. Quit
Choose an option (1-3): 1
Enter student name: Arun
Enter mark (0-100): abc
Invalid mark. Please enter a number from 0 to 100.
Enter mark (0-100): 78
Added Arun successfully.

Student Grade Manager
1. Add student
2. Show results
3. Quit
Choose an option (1-3): 1
Enter student name: Divya
Enter mark (0-100): 59
Added Divya successfully.

Student Grade Manager
1. Add student
2. Show results
3. Quit
Choose an option (1-3): 2

Name            Mark   Grade
----------------------------
Priya             92       A
Arun              78       C
Divya             59       E
----------------------------
Average: 76.3    Highest: 92    Lowest: 59
```

---

## 9. Invalid-input explanation for submission

> I used validation loops to ensure that every student has a non-empty name and a numeric mark between 0 and 100. Empty input, text, negative values, and values above 100 are rejected, and the program asks again instead of crashing. Valid decimal marks are accepted because they are numeric values within the permitted range.

---

## 10. Concepts demonstrated

This project demonstrates:

- Variables and data types
- Lists and dictionaries
- Functions
- Parameters and return values
- `if`, `elif`, and `else`
- `while` loops
- `for` loops
- Exception handling with `try` and `except`
- Input validation
- List comprehensions
- String formatting and alignment
- Basic calculations using `sum()`, `len()`, `max()`, and `min()`
- A standard Python program entry point

---

## 11. Final project flow

```text
Start program
    |
Create an empty students list
    |
Show menu
    |
    +-- Add student
    |      |
    |   Validate name
    |      |
    |   Validate mark
    |      |
    |   Calculate grade
    |      |
    |   Save student record
    |      |
    |   Return to menu
    |
    +-- Show results
    |      |
    |   Check whether records exist
    |      |
    |   Print aligned table
    |      |
    |   Calculate average, highest, and lowest
    |      |
    |   Return to menu
    |
    +-- Quit
           |
       End program
```

The completed program meets the assignment requirements while remaining readable, testable, and safe against common input errors.
