import time
bob = [44, 55, 11]
jos = [1, 2, 1]
harry = [19, 9, 99]
ben = [0, 0, 100]
students = [bob, jos, harry, ben]
print(students)
print(students[0])
print(students[0][1])
names = ["bob", "jos", "harry", "ben"]
func = 1

while func < 4:

    func = int(input("Do you wish to: \nEnter new grades(enter 1)\nFind a students average grade(enter 2)\nFind the highest and lowest grades?(enter 3)\nExit the program?(enter 4)\nEnter here : "))

    if func == 1:
        new_student = int(input(f"Which student do you wish to enter a new grade for?\n{names}\nEnter 0 for first and up one each one along: "))
        grade = int(input("grade: "))
        students[new_student].append(grade)
        print("Grade successfully added!")
        time.sleep(1.5)

    elif func == 2:
        student_avg = int(input(f"Which student do you wish to find the average grade for?\n{names}\nEnter 0 for first and up one each one along: "))
        name = names[student_avg]
        avg = sum(students[student_avg]) / len(students[student_avg])
        print(f"The average grade for {name} is {avg}.")
        time.sleep(1.5)
        
    elif func == 3: 
        student_highlow = int(input(f"Which student do you wish to find the highest and lowest grade for?\n{names}\nEnter 0 for first and up one each one along: "))
        grades_sorted = students[student_highlow]
        grades_sorted.sort()
        print(f"{names[student_highlow]} got {grades_sorted}, with their highest grade as {grades_sorted[len(grades_sorted) - 1]} and their lowest as {grades_sorted[0]}.")
        time.sleep(2)
    else:
        print("Thank you for using this program!")
        time.sleep(1)
