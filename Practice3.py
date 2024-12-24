students = {}

print("Welcome to the Student Grade Management System")
print("You can add students, assign grades, and view report cards.\n")

while True:
    print("Choose an option:")
    print("1. Add a student")
    print("2. Assign grades to a student")
    print("3. Calculate average grades for a student")
    print("4. View report card")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        student_name = input("Enter the student's name: ").strip()
        if student_name in students:
            print(f"{student_name} is already in the system.\n")
        else:
            students[student_name] = []
            print(f"{student_name} has been added to the system.\n")

    elif choice == "2":
        student_name = input("Enter the student's name: ").strip()
        if student_name not in students:
            print(f"{student_name} is not in the system. Add them first.\n")
        else:
            try:
                grade = float(input(f"Enter the grade for {student_name}: "))
                if 0 <= grade <= 100:
                    students[student_name].append(grade)
                    print(f"Grade {grade} has been added for {student_name}.\n")
                else:
                    print("Invalid grade. Please enter a value between 0 and 100.\n")
            except ValueError:
                print("Invalid input. Please enter a numerical grade.\n")

    elif choice == "3":
        student_name = input("Enter the student's name: ").strip()
        if student_name not in students:
            print(f"{student_name} is not in the system. Add them first.\n")
        else:
            grades = students[student_name]
            if grades:
                average = sum(grades) / len(grades)
                print(f"The average grade for {student_name} is {average:.2f}.\n")
            else:
                print(f"No grades recorded for {student_name}.\n")

    elif choice == "4":
        student_name = input("Enter the student's name: ").strip()
        if student_name not in students:
            print(f"{student_name} is not in the system. Add them first.\n")
        else:
            grades = students[student_name]
            if grades:
                print(f"Report card for {student_name}:")
                for i, grade in enumerate(grades, 1):
                    print(f"  Grade {i}: {grade}")
                average = sum(grades) / len(grades)
                print(f"  Average Grade: {average:.2f}\n")
            else:
                print(f"No grades recorded for {student_name}.\n")

    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.\n")
