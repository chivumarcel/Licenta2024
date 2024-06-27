# import Imports.grade_average_service as grade_service

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81,
    'homework_4': 30,
    'homework_5': 50
}

def calculate_homework (homework_assignment_arg):
    sum_of_grades = 0
    for homework in homework_assignment_arg.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades / len(homework_assignment_arg),2)
    print(final_grade)
calculate_homework(homework_assignment_grades)

# grade_service.calculate_homework(homework_assignment_grades)


















