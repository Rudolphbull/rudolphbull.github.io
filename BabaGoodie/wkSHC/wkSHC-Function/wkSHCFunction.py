# Programmer-Mr.Olayinka Goodluck
# Student-ID-2144303.


class Grade:
    def __init__(self, int_exam, int_assign):
        self.int_exam = int_exam
        self.int_assign = int_assign

    def calcGrade(self):
        sum_of_marks = self.int_exam + self.int_assign
        average_mark = int(sum_of_marks / 2)
        if average_mark < 40:
            return f"Your overall grade is: F"
        elif average_mark >= 40 and average_mark < 50:
            return f"Your overall grade is: D"
        elif average_mark >= 50 and average_mark < 60:
            return f"Your overall grade is: C"
        elif average_mark >= 60 and average_mark < 70:
            return f"Your overall grade is: B"
        elif average_mark >= 70:
            return f"Your overall grade is: A"


# This is to check entered exam mark


def check_exam_mark(int_exam):
    if int_exam.isdigit() and int(int_exam) <= 100:
        return int(int_exam)
    elif int_exam.isalpha() or len(int_exam) == 0 or int(int_exam) > 100:
        while int_exam.isalpha() or len(int_exam) == 0 or int(int_exam) > 100:
            int_exam = input("Re-enter the exam mark: ")
            if int_exam.isdigit() and int(int_exam) <= 100:
                return int(int_exam)
    else:
        return int(int_exam)

# This is to check entered exam mark


def check_assignment_mark(int_assign):
    if int_assign.isdigit() and int(int_assign) <= 100:
        return int(int_assign)
    elif int_assign.isalpha() or len(int_assign) == 0 or int(int_assign) > 100:
        while int_assign.isalpha() or len(int_assign) == 0 or int(int_assign) > 100:
            int_assign = input("Re-enter the assignment mark: ")
            if int_assign.isdigit() and int(int_assign) <= 100:
                return int(int_assign)
    else:
        return int(int_assign)


int_exam = input("Please enter exam mark: ")
int_exam = check_exam_mark(int_exam)

int_assign = input("Please enter assignment mark: ")
int_assign = check_assignment_mark(int_assign)

check_grade = Grade(int_exam, int_assign)

print(check_grade.calcGrade())
