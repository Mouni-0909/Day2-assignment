
# Student Marks Management System

# Step 1: Create an empty list to store student details
students = []


# Step 2: Function to calculate student grade
def get_grade(mark):

    if mark >= 90:
        return "A"

    elif mark >= 80:
        return "B"

    elif mark >= 70:
        return "C"

    elif mark >= 60:
        return "D"

    else:
        return "E"


# Step 3: Function to add student details
def add_student():

    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    try:
        mark = float(input("Enter student mark (0-100): "))

        if mark < 0 or mark > 100:
            print("Error: Mark must be between 0 and 100.")
            return

        # Calculate grade
        grade = get_grade(mark)

        # Store student details
        student = {
            "name": name,
            "mark": mark,
            "grade": grade
        }

        students.append(student)

        print("Student added successfully!")

    except ValueError:
        print("Error: Please enter a valid number.")


# Step 4: Function to display student results
def show_results():

    if len(students) == 0:
        print("No student records available.")
        return

    print("\n==============================================")
    print("             STUDENT MARKS REPORT")
    print("==============================================")

    print(f"{'Name':<20} {'Mark':>10} {'Grade':>10}")
    print("----------------------------------------------")

    for student in students:

        print(
            f"{student['name']:<20} "
            f"{student['mark']:>10.2f} "
            f"{student['grade']:>10}"
        )

    print("----------------------------------------------")

    # Calculate class statistics
    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Class Average : {average:.2f}")
    print(f"Highest Mark  : {highest:.2f}")
    print(f"Lowest Mark   : {lowest:.2f}")

    print("==============================================")


# Step 5: Main menu loop
def main():

    while True:

        print("\n===== STUDENT MARKS MANAGEMENT =====")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            show_results()

        elif choice == "3":

            print("Thank you! Exiting program.")
            break

        else:

            print("Invalid choice! Please enter 1, 2 or 3.")


# Step 6: Start the program
if __name__ == "__main__":
    main()