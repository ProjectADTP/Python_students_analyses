SUCCESS_THRESHOLD = 75

def add_new_student(student):
    students.append(student)


def remove_worst_student():
    if not students:
        print("В списке нет студентов для удаления!")

        return
    else:
        students.remove(find_worst_student())


def is_student_successful(average_grade):
    return average_grade >= SUCCESS_THRESHOLD

def find_worst_student():
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


def calculate_overall_average_grades():
    if not students:
        return None

    overall_average_grades = 0

    for student in students:
        overall_average_grades += calculate_average_grade(student.get("grades"))

    return overall_average_grades / len(students)


def print_student_info(student):
    student_name = student["name"]
    average_grades = calculate_average_grade(student.get("grades"))
    is_successful = is_student_successful(average_grades)

    print(f"Студент: {student_name}\nСредний балл: {average_grades}\n"
          f"Статус: {"Успешен" if is_successful == True else "Не успешен"}\n")


def print_overall_average_grades():
    overall_average_grades = calculate_overall_average_grades()

    if overall_average_grades is not None:
        print("Общий средний балл студентов:", overall_average_grades)
    else:
        print("Список пуст!")

def print_all_students_info():
    for student in students:
        print_student_info(student)

    print_overall_average_grades()


students = [
        {"name": "Maxim", "grades": [60, 75, 68, 90, 87]},
        {"name": "Albert", "grades": [76, 63, 84, 61, 67]},
        {"name": "Andrey", "grades": [69, 69, 70, 69, 72]},
        {"name": "Alexander", "grades": [75, 75, 75, 75, 75]},
        {"name": "Ilona", "grades": [85, 65, 60, 77, 87]},
    ]

print_all_students_info()

add_new_student({"name": "Michael", "grades": [80, 75, 80, 90, 90]})

print("-" * 25 + "\nДобавлен новый студент!\n" + "-" * 25)
print_all_students_info()

remove_worst_student()

print("-" * 25 + "\nУдалён худший студент!\n" + "-" * 25)
print_all_students_info()