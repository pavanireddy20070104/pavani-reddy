#creating grades list
grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
students_got_grade_a = 0
students_got_grade_b = 0
students_got_grade_c = 0
students_got_below70 = 0
for grade in grades:
    if grade >= 90:
        print("got A")
        students_got_grade_a +=1
    elif 80 <= grade <= 89:
        print("got B")
        students_got_grade_b += 1
    elif 70 <= grade <= 79:
        print("got C")
        students_got_grade_c += 1
    else:
        print("Below 70")
        students_got_below70 += 1
print("count of the students got grade_a" ,students_got_grade_a)
print("count of the students got grade_b" , students_got_grade_b)
print("count of the students got grade_c" ,students_got_grade_c)
print("count of the students got below 70" ,students_got_below70)
