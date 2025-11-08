# ----------------------------
# Student Registration & Quiz System
# ----------------------------

# قائمة لتخزين بيانات الطلاب
students = []
# Task 1: Register Student
def register_student():
    print("\n--- Student Registration ---")
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    subjects_input = input("Enter favorite subjects (comma-separated): ").strip()
    subjects = tuple(subject.strip() for subject in subjects_input.split(','))
    student = {
        "name": name,
        "age": age,
        "subjects": subjects,
        "score": 0
    }

    students.append(student)

    print(f"\n✅ {name} has been successfully registered!\n")

# Task 2: Start Quiz
def start_quiz(student):
    print(f"\n--- Starting Quiz for {student['name']} ---")

    questions = [
        {"question": "What keyword is used to define a function in Python?", "answer": "def"},
        {"question": "What data type is used to store True or False values?", "answer": "bool"},
        {"question": "Which symbol is used for comments in Python?", "answer": "#"}
    ]

    score = 0

    for q in questions:
        user_answer = input(f"{q['question']} ").strip().lower()
        if user_answer == q["answer"].lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    student["score"] = score
    print(f"🎯 {student['name']} scored {score}/{len(questions)}\n")

# Task 3: Show Report
def show_report():
    print("\n--- Students Report ---")
    if not students:
        print("No students registered yet.\n")
        return

    for s in students:
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Subjects: {', '.join(s['subjects'])}")
        print(f"Score: {s['score']}\n")


# Task 4: Main Menu
def main_menu():
    while True:
        print("Main Menu:")
        print("1. Register Student")
        print("2. Start Quiz")
        print("3. Show Report")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_student()

        elif choice == "2":
            if not students:
                print("\nNo students registered yet. Please register first.\n")
                continue

            name = input("Enter student name to start quiz: ").strip()
            found_student = next((s for s in students if s["name"].lower() == name.lower()), None)

            if found_student:
                start_quiz(found_student)
            else:
                print(f"\nStudent '{name}' not found.\n")

        elif choice == "3":
            show_report()

        elif choice == "4":
            with open("students.txt", "w") as file:
                for s in students:
                    file.write(str(s) + "\n")
            print("\nAll data saved to students.txt ✅")
            print("Exiting the system... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()
