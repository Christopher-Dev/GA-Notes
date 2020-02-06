list_of_students = ["John", "Sara", "Cassie"]

answer = ["yes", "Yes", "YES", "Y"]

name = input("Type name of student: ")


if name not in list_of_students:
    print("Student is not enrolled.")



    enrolling = input("Would you like to enroll? ")

    if enrolling in answer:
        list_of_students.append(input("Enter name now: "))
        print(list_of_students)
    else:
        print("Student is now enrolled. Thank you for enrolling your student. We can take it from here.")

    enrolling = input("Would you like to enroll another student? ")

    if enrolling in answer:
        list_of_students.append(input("Enter second name now: "))
        print(list_of_students)
        print("Here is the roster for 2020.")
    else:
        print("Student is enrolled. Thank you for enrolling your student. We can take it from here.")
else:
    print("Student is enrolled. Thank you for enrolling your student. We can take it from here.")