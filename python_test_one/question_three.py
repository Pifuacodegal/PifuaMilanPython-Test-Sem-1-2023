
# list
student_marks = [78, 83, 90, 88, 75]
def sum_of_student_marks(m, n, o, p, q):
    output = m + n + o + p + q
    print(f" The sum of student marks {m}, {n}, {o}, {p}, {q} is {output}")
sum_of_student_marks(78, 83, 90,  88, 75) 

student_marks = [78, 83, 90, 88, 75]
first_mark = student_marks[0]
last_mark = student_marks[4]
print(first_mark)
print(last_mark)

student_marks = [78, 83, 90, 88, 75]
student_marks.append(96)
print(student_marks)

student_marks = [78, 83, 90, 88, 75]
student_marks[0] = 87
print(student_marks)