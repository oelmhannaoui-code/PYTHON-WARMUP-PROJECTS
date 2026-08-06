# TO DO LIST
tasks = []

def welcome():
    print('**TO DO LIST**')
def menu():
    print('1. Add task')
    print('2. View tasks')
    print('3. Remove task')
    print('4. Mark task as completed')
    print('5. Exit')
def add_task():
    task = input('Add task: ')
    done = input('Done? (true/false): ').lower() == 'true'

    tasks.append({'task': task , 'done': done })
    print(f'{task} added successfully!')

def view_tasks():
    print('\nyour tasks :')
    for task in tasks:
        if task['done']:
         print(task['task'],'-Done')
        else:
            print(task['task'],'-Not Done')
def remove_task():
    task_name = input('Remove task: ')

    for task in tasks:
     if task ['task'].lower() == task_name.lower():
        tasks.remove(task)
        print(f'{task_name} removed')
        return

    print('Task not found')
def mark_task():
    complete_task = input('Mark task: ')
    for task in tasks:
        if task['task'].lower() == complete_task.lower():
            task['done'] = True
            print(f'{complete_task} marked successfully!')
            return
    else:
        print('Task not found')

welcome()
choice = 0
while choice != 5:
    menu()
    choice = int(input('Enter your choice: '))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        mark_task()
    elif:
        print('BYE BYE DR.GREENTHUMB!')
    else:
      print('Invalid choice!')
