from database import Database
from student_service import StudentService

def main():
    service = StudentService(Database())

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student\n2. View All Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                sid = int(input("Student ID: "))
                name = input("Name: ").strip()
                age = int(input("Age: "))
                course = input("Course: ").strip()
                if not name or not course:
                    print("Name and Course cannot be empty")
                    continue
                service.add_student(sid, name, age, course)
                print("Student added successfully")

            elif choice == "2":
                students = service.get_all_students()
                if not students:
                    print("No students found")
                else:
                    for student in students:
                        print(student)

            elif choice == "3":
                sid = int(input("Student ID: "))
                result = service.get_student(sid)
                print(result if result else "Not found")

            elif choice == "4":
                sid = int(input("Student ID: "))
                name = input("New name: ").strip()
                age = int(input("New age: "))
                course = input("New course: ").strip()
                if service.update_student(sid, name, age, course):
                    print("Student updated")
                else:
                    print("Student not found")

            elif choice == "5":
                sid = int(input("Student ID: "))
                if service.delete_student(sid):
                    print("Student deleted")
                else:
                    print("Student not found")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Error: Please enter numbers for ID and Age correctly")
        except Exception as error:
            print("Error:", error)

if __name__ == "__main__":
    main()