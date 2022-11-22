# Programmer-Mr.Olayinka Goodluck
# Student-ID-2144303.


confirmed_exam_mark = " "
exam_mark = input("Please enter exam mark: ")
if exam_mark.isdigit() and int(exam_mark) <= 100:
        confirmed_exam_mark = int(exam_mark)

elif exam_mark.isalpha() or len(exam_mark) == 0 or int(exam_mark) > 100:
    while exam_mark.isalpha() or len(exam_mark) == 0 or int(exam_mark) > 100:
        exam_mark= input("Re-enter the mark : ")
        if exam_mark.isdigit() and int(exam_mark) <= 100:
             confirmed_exam_mark = int(exam_mark)

confirmed_assignment_mark = " "
assignment_mark = input("Please enter assignment mark: ")

if assignment_mark.isdigit() and int(assignment_mark) <= 100:
       confirmed_assignment_mark= int(assignment_mark)

elif assignment_mark.isalpha() or len(assignment_mark) == 0 or int(assignment_mark) > 100:
    while assignment_mark.isalpha() or len(assignment_mark) == 0 or int(assignment_mark) > 100:
        assignment_mark = input("Re-enter the mark: ")
        if assignment_mark.isdigit() and int(assignment_mark) <= 100:
          confirmed_assignment_mark = int(assignment_mark)

sum_of_marks = confirmed_assignment_mark + confirmed_exam_mark
average_mark = (sum_of_marks / 2)

if average_mark < 40:
    print("Your overall grade is: F")
elif 40 <= average_mark < 50:
    print("Your overall mark is: D")
elif 50 <= average_mark < 60:
    print("Your overall mark is: C")
elif 60 <= average_mark < 70:
    print("Your overall mark is: B")
else:
    print("Your overall grade is: A")
