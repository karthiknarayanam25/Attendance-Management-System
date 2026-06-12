# Attendance Management System
students = {}

while True:
    print("\n===== ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students[name] = "Not Marked"
        print(f"{name} added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students available!")
        else:
            for name in students:
                attendance = input(f"{name} (P/A): ").upper()

                if attendance == "P":
                    students[name] = "Present"
                elif attendance == "A":
                    students[name] = "Absent"
                else:
                    print("Invalid input!")
            print("Attendance marked successfully!")

    elif choice == "3":
        print("\n----- Attendance Report -----")

        if len(students) == 0:
            print("No records found!")
        else:
            for name, status in students.items():
                print(f"{name} : {status}")

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")