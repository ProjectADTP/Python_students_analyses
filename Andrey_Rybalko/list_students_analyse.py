def add_new_student():
    students.append({"name": "Michael", "grades": [80, 75, 80, 90, 90]})

    print("-" * 25 + "\nДобавлен новый студент!\n" + "-" * 25)
    calculate_students_grades()


def remove_worst_student():
    students.remove(find_worst_student())

    print("-" * 25 + "\nУдалён студент с наименьшим средним баллом!\n" + "-" * 25)
    calculate_students_grades()


def find_worst_student():
    worst_student = students[0]
    for student in students:
        if calculate_average_grades(student.get("grades")) < calculate_average_grades(worst_student.get("grades")):
            worst_student = student

    return worst_student


def calculate_average_grades(grades):
    return sum(grades) / len(grades)


def calculate_students_grades():
    overall_grades = 0
    for student in students:
        average_grades = calculate_average_grades(student.get("grades"))

        print_student_info(student['name'], average_grades, True if average_grades >= 75 else False)

        overall_grades += average_grades

    print_overall_average_grades(overall_grades, len(students))


def print_student_info(student_name, average_grades, is_successful):
    print(f"Студент: {student_name}\nСредний балл: {average_grades}\n"
          f"Статус: {"Успешен" if is_successful == True else "Не успешен"}\n")


def print_overall_average_grades(overall_average_grades, number_of_students):
    print("Общий средний балл студентов:", overall_average_grades/ number_of_students)


def check_successful_of_students():
    calculate_students_grades()
    add_new_student()
    remove_worst_student()


students = [
        {"name": "Maxim", "grades": [60, 75, 68, 90, 87]},
        {"name": "Albert", "grades": [76, 63, 84, 61, 67]},
        {"name": "Andrey", "grades": [69, 69, 70, 69, 72]},
        {"name": "Alexander", "grades": [75, 75, 75, 75, 75]},
        {"name": "Ilona", "grades": [85, 65, 60, 77, 87]},
    ]

check_successful_of_students()