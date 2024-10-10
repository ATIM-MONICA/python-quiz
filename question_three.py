#Qn3. WITI has tasked you to automate a simple grading system.
# As a python student, write a program using to display the grades that
# The students will be receiving based on the marks scored in a subject.
# The grades are:
# 90% - 100% Grade is A
# 80% - 89% Grade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50% - 59% Grade is E
# <50% Fail
marks_scored = float(input("Enter marks scored (0-100): "))
if 0 <= marks_scored <= 100:
    if marks_scored >= 90:
        grade = 'A'
        print("Grade:", grade)
    elif marks_scored >= 80:
        grade = 'B'
        print("Grade:", grade)
    elif marks_scored >= 70:
        grade = 'C'
        print("Grade:", grade)
    elif marks_scored >= 60:
        grade = 'D'
        print("Grade:", grade)
    elif marks_scored >= 50:
        grade = 'E'
        print("Grade:", grade)
    elif marks_scored < 50:
        grade = 'Fail'
        print("Grade:", grade)
else:
    print("Invalid marks. Please enter the value between o and 100.")
    