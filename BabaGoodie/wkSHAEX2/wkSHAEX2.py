# Programmer-Mr.OlayinkaGoodluck
# Student-ID-2144303.

try:

    confirmed_first_student = " "
    first_student = input("Enter the name of first student: ").title()
    # To check user does not enter a blank name for first student
    if len(first_student) == 0:
        while len(first_student) == 0:
            first_student = input("First student's name can not be blank, Enter the name of first student? ").title()
            if len(first_student) > 0:
                confirmed_first_student = first_student
    else:
        confirmed_first_student = first_student
    # To check user does not enter a digit for first students's name
    if first_student.isdigit():
        while first_student.isdigit():
            first_student = input("First Student's name can not contain number, Enter the name of first student? ").title()
            if not first_student.isdigit():
                confirmed_first_student = first_student

    else:
        confirmed_first_student = first_student
    #  To check user does not enter a blank name for second student
    confirmed_second_student = " "
    second_student = input("Enter the name of second student: ").title()
    if len(second_student) == 0:
        while len(second_student) == 0:
            second_student = input("Second student's name can not be blank, Enter the name of second student? ").title()
            if len(second_student) > 0:
                confirmed_second_student = second_student
    else:
        confirmed_second_student = second_student
    # To check user does not enter a digit for second students's name
    if second_student.isdigit():
        while second_student.isdigit():
            second_student = input(
                "Second Student's name can not contain number, Enter the name of second student? ").title()
            if not second_student.isdigit():
                confirmed_second_student = second_student
    # To check user does not enter a blank name for third student
    confirmed_third_student = " "
    third_student = input("Enter the name of third student: ").title()
    if len(third_student) == 0:
        while len(third_student) == 0:
            third_student = input("Third student's name can not be blank, Enter the name of third student? ").title()
            if len(third_student) > 0:
                confirmed_third_student = third_student
    else:
        confirmed_third_student = third_student
    # To check user does not enter a digit for third students's name
    if third_student.isdigit():
        while third_student.isdigit():
            third_student = input("Third Student's name can not contain number, Enter the name of third student? ").title()
            if not third_student.isdigit():
                confirmed_third_student = third_student
    # To check user does not enter blank for first student exam grade
    first_student_exam_grade = " "
    exam_grade_first_student = int(input(f'Please enter {confirmed_first_student}\'s exam grade: '))
    if len(str(exam_grade_first_student)) == 0:
        while len(str(exam_grade_first_student)) == 0:
            exam_grade_first_student = int(input(f'Exam grade of first student can not be blank, Please enter '
                                                 f'{confirmed_first_student}\'s exam grade: '))
            if len(str(exam_grade_first_student)) > 0:
                first_student_exam_grade = exam_grade_first_student
    else:
        first_student_exam_grade = exam_grade_first_student
    # To check user does not enter digit/number for first student exam grade
    if str(exam_grade_first_student).isalpha():
        while str(exam_grade_first_student).isalpha():
            exam_grade_first_student = int(input(f'Exam grade of first student can not be letters, Please enter '
                                                 f'{confirmed_first_student}\'s exam grade: '))
            if not str(exam_grade_first_student).isalpha():
                first_student_exam_grade = exam_grade_first_student
    else:
        first_student_exam_grade = exam_grade_first_student
    #  To check user does not enter a number greater than 70 first student exam grade
    if exam_grade_first_student > 70:
        while exam_grade_first_student > 70:
            exam_grade_first_student = int(input(f'Exam grade should be less than or equal to 70. Please enter '
                                                 f'{confirmed_first_student}\'s exam grade: '))
            if exam_grade_first_student <= 70:
                first_student_exam_grade = exam_grade_first_student
    else:
        first_student_exam_grade = exam_grade_first_student
    #  To check user does not enter a blank for first student coursework grade
    first_student_coursework_grade = " "
    coursework_grade_first_student = int(input(f'Please enter {confirmed_first_student}\'s coursework grade: '))
    if len(str(coursework_grade_first_student)) == 0:
        while len(str(coursework_grade_first_student)) == 0:
            coursework_grade_first_student = int(input(f'Coursework grade of first student can not be blank, Please enter '
                                                       f'{confirmed_first_student}\'s coursework grade: '))
            if len(str(coursework_grade_first_student)) > 0:
                first_student_coursework_grade = coursework_grade_first_student
    else:
        first_student_coursework_grade = coursework_grade_first_student
    #  To check user does not enter a digit/number for first student coursework grade
    if str(coursework_grade_first_student).isalpha():
        while str(coursework_grade_first_student).isalpha():
            coursework_grade_first_student = int(
                input(f'Coursework grade of first student can not be letters, Please enter '
                      f'{confirmed_first_student}\'s coursework grade: '))
            if not str(coursework_grade_first_student).isalpha():
                first_student_coursework_grade = coursework_grade_first_student
    else:
        first_student_coursework_grade = coursework_grade_first_student
    #  To check user does not enter a number higher than 30 for first student coursework grade
    if coursework_grade_first_student > 30:
        while coursework_grade_first_student > 30:
            coursework_grade_first_student = int(input(f'Coursework grade should be less than or equal to 30. Please enter '
                                                       f'{confirmed_first_student}\'s coursework grade: '))
            if coursework_grade_first_student <= 30:
                first_student_coursework_grade = coursework_grade_first_student
    else:
        first_student_coursework_grade = coursework_grade_first_student
    #
    second_student_exam_grade = " "
    exam_grade_second_student = int(input(f'Please enter {confirmed_second_student}\'s exam grade: '))
    if len(str(exam_grade_second_student)) == 0:
        while len(str(exam_grade_second_student)) == 0:
            exam_grade_second_student = int(input(f'Exam grade of second student can not be blank, Please enter '
                                                  f'{confirmed_second_student}\'s exam grade: '))
            if len(str(exam_grade_second_student)) > 0:
                second_student_exam_grade = exam_grade_second_student
    else:
        second_student_exam_grade = exam_grade_second_student
    if str(exam_grade_second_student).isalpha():
        while str(exam_grade_second_student).isalpha():
            exam_grade_second_student = int(input(f'Exam grade of second student can not be letters, Please enter '
                                                  f'{confirmed_second_student}\'s exam grade: '))
            if not str(exam_grade_second_student).isalpha():
                second_student_exam_grade = exam_grade_second_student
    else:
        second_student_exam_grade = exam_grade_second_student
    if exam_grade_second_student > 70:
        while exam_grade_second_student > 70:
            exam_grade_second_student = int(input(f'Exam grade should be less than or equal to 70. Please enter '
                                                  f'{confirmed_second_student}\'s exam grade: '))
            if exam_grade_second_student <= 70:
                second_student_exam_grade = exam_grade_second_student
    else:
        second_student_exam_grade = exam_grade_second_student
    second_student_coursework_grade = " "
    coursework_grade_second_student = int(input(f'Please enter {confirmed_second_student}\'s coursework grade: '))
    if len(str(coursework_grade_second_student)) == 0:
        while len(str(coursework_grade_second_student)) == 0:
            coursework_grade_second_student = int(
                input(f'Coursework grade of second student can not be blank, Please enter '
                      f'{confirmed_second_student}\'s coursework grade: '))
            if len(str(coursework_grade_second_student)) > 0:
                second_student_coursework_grade = coursework_grade_second_student
    else:
        second_student_coursework_grade = coursework_grade_second_student
    if str(coursework_grade_second_student).isalpha():
        while str(coursework_grade_second_student).isalpha():
            coursework_grade_second_student = int(
                input(f'Coursework grade of second student can not be letters, Please enter '
                      f'{confirmed_second_student}\'s coursework grade: '))
            if str(coursework_grade_second_student).isalpha():
                second_student_coursework_grade = coursework_grade_second_student
    else:
        second_student_coursework_grade = coursework_grade_second_student
    if coursework_grade_second_student > 30:
        while coursework_grade_second_student > 30:
            coursework_grade_second_student = int(
                input(f'Coursework grade should be less than or equal to 30. Please enter '
                      f'{confirmed_second_student}\'s coursework grade: '))
            if coursework_grade_second_student <= 30:
                second_student_coursework_grade = coursework_grade_second_student
    else:
        second_student_coursework_grade = coursework_grade_second_student
    #
    third_student_exam_grade = " "
    exam_grade_third_student = int(input(f'Please enter {confirmed_third_student}\'s exam grade: '))
    if len(str(exam_grade_third_student)) == 0:
        while len(str(exam_grade_third_student)) == 0:
            exam_grade_third_student = int(input(f'Exam grade of third student can not be blank, Please enter '
                                                 f'{confirmed_third_student}\'s exam grade: '))
            if len(str(exam_grade_third_student)) > 0:
                third_student_exam_grade = exam_grade_third_student
    else:
        third_student_exam_grade = exam_grade_third_student
    if str(exam_grade_third_student).isalpha():
        while str(exam_grade_third_student).isalpha():
            exam_grade_third_student = int(input(f'Exam grade of third student can not be letters, Please enter '
                                                 f'{confirmed_third_student}\'s exam grade: '))
            if not str(exam_grade_third_student).isalpha():
                third_student_exam_grade = exam_grade_third_student
    if exam_grade_third_student > 70:
        while exam_grade_third_student > 70:
            exam_grade_second_student = int(input(f'Exam grade should be less than or equal to 70. Please enter '
                                                  f'{confirmed_third_student}\'s exam grade: '))
            if exam_grade_third_student <= 70:
                third_student_exam_grade = exam_grade_third_student
    else:
        third_student_exam_grade = exam_grade_third_student
    third_student_coursework_grade = " "
    coursework_grade_third_student = int(input(f'Please enter {confirmed_third_student}\'s coursework grade: '))
    if len(str(coursework_grade_third_student)) == 0:
        while len(str(coursework_grade_third_student)) == 0:
            coursework_grade_third_student = int(input(f'Coursework grade of third student can not be blank, Please enter '
                                                       f'{confirmed_third_student}\'s coursework grade: '))
            if len(str(coursework_grade_third_student)) > 0:
                third_student_coursework_grade = coursework_grade_third_student
    else:
        third_student_coursework_grade = coursework_grade_third_student
    if str(coursework_grade_third_student).isalpha():
        while str(coursework_grade_third_student).isalpha():
            coursework_grade_third_student = int(
                input(f'Coursework grade of third student can not be letters, Please enter '
                      f'{confirmed_third_student}\'s coursework grade: '))
            if not str(coursework_grade_third_student).isalpha():
                third_student_coursework_grade = coursework_grade_third_student
    if coursework_grade_third_student > 30:
        while coursework_grade_third_student > 30:
            coursework_grade_third_student = int(input(f'Coursework grade should be less than or equal to 30. Please enter '
                                                       f'{confirmed_third_student}\'s coursework grade: '))
            if coursework_grade_third_student <= 30:
                third_student_coursework_grade = coursework_grade_third_student
    else:
        third_student_coursework_grade = coursework_grade_third_student
    a = confirmed_first_student = first_student
    b = confirmed_second_student = second_student
    c = confirmed_third_student = third_student
    a1 = first_student_exam_grade + first_student_coursework_grade
    b1 = second_student_exam_grade + second_student_coursework_grade
    c1 = third_student_exam_grade + third_student_coursework_grade
    d1 = a1 + b1 + c1  # sum of overall grade of three students
    overall_grade_first_student = a1
    overall_grade_second_student = b1
    overall_grade_third_student = c1
    Average_of_three_students = d1 / 3
    new_avg_of_three_students = round(Average_of_three_students, 1)

    print('*' * 23)
    print('*' * 3, f'Students\' grade', '*' * 3)
    print('*' * 23)
    print('Student', 'Exam', 'Course work', 'Overall grade')
    print(f"{a}  {exam_grade_first_student}  {coursework_grade_first_student} {a1}")
    print(f"{b} {exam_grade_second_student} {coursework_grade_second_student} {b1}")
    print(f"{c} {exam_grade_third_student} {coursework_grade_third_student} {c1}")
    print(f"The average grade for the three students is: {new_avg_of_three_students}")
except ValueError:
    print("Sorry, Invalid input!!!!Exam grade and Coursework grade can not be letters, and can not contain decimals.")
