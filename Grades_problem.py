bob = [44, 55, 11]
jos = [1, 2, 1]
harry = [19, 9, 99]
ben = [0, 0, 100]
students = [bob, jos, harry, ben]
print(students)
print(students[0])
print(students[0][1])
names = ["bob", "jos", "harry", "ben"]
go = 1

func = int(input("Do you wish to: \nEnter new grades(enter 1)\nFind a students average grade(enter 2)\nFind the highest and lowest grades?(enter 3)"))

if func == 1:
    while go == 1:
        new_student = int(input(f"Which student do you wish to enter a new grade for?\n{names}\nEnter 0 for first and up one each one along: "))
        grade = int(input("grade: "))
        students[new_student].append(grade)
        print(students[new_student])
        go = int(input("Do you want to enter another grade for a student: Enter 1 for yes or 2 for no: "))

elif func == 2:
    student_avg = int(input(f"Which student do you wish to find the average grade for?\n{names}\nEnter 0 for first and up one each one along: "))
    name = names[student_avg]
    avg = sum(students[student_avg]) / len(students[student_avg])
    print(f"The average grade for {name} is {avg}.")
    
else: 
    student_highlow = int(input(f"Which student do you wish to find the highest and lowest grade for?\n{names}\nEnter 0 for first and up one each one along: "))
    name = names[student_highlow]
    print(list.sort(names[student_highlow]))
