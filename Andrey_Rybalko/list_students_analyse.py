SUCCESS_THRESHOLD = 75
def create_student_list():
    students = [
        {"name": "Maxim", "grades": [60, 75, 68, 90, 87]},
        {"name": "Albert", "grades": [76, 63, 84, 61, 67]},
        {"name": "Andrey", "grades": [69, 69, 70, 69, 72]},
        {"name": "Alexander", "grades": [75, 75, 75, 75, 75]},
        {"name": "Ilona", "grades": [85, 65, 60, 77, 87]},
    ]

    return students


def add_new_student(student, students):
    students.append(student)


def remove_worst_student(students):
    if not students:
        print("В списке нет студентов для удаления!")

        return
    else:
        students.remove(find_worst_student(students))


def find_worst_student(students):
    if not students:
        return None

    worst = students[0]
    worst_average = calculate_average_grade(worst.get("grades"))

    for student in students[1:]:
        average = calculate_average_grade((student.get("grades")))
        if average < worst_average:
            worst = student
            worst_average = average

    return worst


def calculate_average_grade(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print("Внимание, попытка деления на 0!")
        return 0


def calculate_overall_average_grades(students):
    if not students:
        return None

    overall_average_grades = 0

    for student in students:
        overall_average_grades += calculate_average_grade(student.get("grades"))

    return overall_average_grades / len(students)


def print_student_info(student):
    student_name = student["name"]
    average_grade = calculate_average_grade(student.get("grades"))

    print(f"Студент: {student_name}\nСредний балл: {average_grade}\n"
          f"Статус: {"Успешен" if average_grade >= SUCCESS_THRESHOLD else "Не успешен"}\n")


def print_overall_average_grades(students):
    overall_average_grades = calculate_overall_average_grades(students)

    if overall_average_grades is not None:
        print("Общий средний балл студентов:", overall_average_grades)
    else:
        print("Список пуст!")


def print_all_students_info(students):
    for student in students:
        print_student_info(student)

    print_overall_average_grades(students)


student_list = create_student_list()

print_all_students_info(student_list)

add_new_student({"name": "Michael", "grades": [80, 75, 80, 90, 90]}, student_list)
print("-" * 25 + "\nДобавлен новый студент!\n" + "-" * 25)

print_all_students_info(student_list)

remove_worst_student(student_list)
print("-" * 25 + "\nУдалён худший студент!\n" + "-" * 25)

print_all_students_info(student_list)