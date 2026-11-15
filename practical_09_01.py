Grades = {"Дмитро": [9, 12, 9, 9, 8], "Іван": [1, 3, 4, 1, 2], "Ілля": [7, 8, 12, 11, 9], "Матвій": [5, 7, 3, 2, 1]}
min = 6
def avg_grade(arr):
     return sum(arr) // len(arr)
def has_passed(average):
    return average >= min
def report(student, average, passed):
    status = "здав на прохідний бал" if passed else "не здав на прохідний бал"
    print(f"Студент {student} {status} із середнім балом: {average}")
def analyze(student, arr):
    average = avg_grade(arr)
    passed = has_passed(average)
    report(student, average, passed)
def main(grades):
    for student, arr in grades.items():
        analyze(student, arr)

main(Grades)