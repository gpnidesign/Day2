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
    return str(int(mark)) if mark.is_integer() else f"{mark:.2f}".rstrip("0").rstrip(".")


def add_student(students):
    """Read, validate, and store one student record."""
    name = get_valid_name()
    mark = get_valid_mark()
    students.append({"name": name, "mark": mark, "grade": get_grade(mark)})
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
        print(f'{student["name"]:<{name_width}} {mark_text:>7}   {student["grade"]:>5}')

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
