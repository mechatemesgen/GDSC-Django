def add_student(database):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")


    database[name] = {'Age': age, 'Grade': grade}
    print(f"{name} added to the database.")

def view_student(database):
    name = input("Enter student name to view details: ")
    student = database.get(name)

    if student:
        print(f"\nStudent Details for {name}:")
        print(f"Age: {student['Age']}")
        print(f"Grade: {student['Grade']}")
    else:
        print(f"Student {name} not found in the database.")

def list_all_students(database):
    print("\nList of All Students:")
    for name, details in database.items():
        print(f"{name}: Age - {details['Age']}, Grade - {details['Grade']}")

def update_student(database):
    name = input("Enter student name to update details: ")
    student = database.get(name)

    if student:
        print(f"\nCurrent Details for {name}:")
        print(f"Age: {student['Age']}")
        print(f"Grade: {student['Grade']}")
        
   
        age = int(input("Enter updated age: "))
        grade = input("Enter updated grade: ")

        database[name]['Age'] = age
        database[name]['Grade'] = grade

        print(f"Details for {name} updated.")
    else:
        print(f"Student {name} not found in the database.")

def delete_student(database):
    name = input("Enter student name to delete: ")
    if name in database:
        del database[name]
        print(f"{name} deleted from the database.")
    else:
        print(f"Student {name} not found in the database.")

def main():
    student_database = {}

    while True:
        print("\nStudent Database Program")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student(student_database)
        elif choice == '2':
            view_student(student_database)
        elif choice == '3':
            list_all_students(student_database)
        elif choice == '4':
            update_student(student_database)
        elif choice == '5':
            delete_student(student_database)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
