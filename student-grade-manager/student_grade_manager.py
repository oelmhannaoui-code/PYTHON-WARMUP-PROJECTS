students = []
def welcome():
    print('**STUDENT GRADE MANAGER**')

def menu():
    print('1. Add Student')
    print('2. Display Students')
    print('3. Remove Student')
    print('4. Calculate average grade')
    print('5. Exit')

def add_student():
 name = input('enter student name: ')
 grade = int(input('enter grade: '))

 student = { 'name': name, 'grade': grade}

 students.append(student)
 print(f'{name} added successfully!')


def display_students():
    print('\nStudents :')
    for student in students:
        print(f'- {student["name"]} ')

def remove_student():
    name = input('enter student to remove: ')
    for student in students:       # need to loop through all students
       if student['name'] == name:
        students.remove(student)
        print(f'{student["name"]} removed successfully!')
        break
    else:
       print('student not found')

def calculate_average():
    if len(students) == 0:
        print('no students found')
        return
    total = 0
    for student in students:
        total += student['grade'] # Add all grades 1st
    average = total / len(students) # Calculate once at the end!

    print(f'average grade is {average}') # Print once at the end 


welcome()
choice = 0
while choice != 5:
   menu()
   choice = int(input('enter choice: '))
   if choice == 1:
    add_student()
   elif choice == 2:
    display_students()
   elif choice == 3:
    remove_student()
   elif choice == 4:
    calculate_average()

else:
    print('Shutting down!')
