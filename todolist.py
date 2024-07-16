# Define a dictionary to store tasks
tasks = {}

def show_menu():
    print("\n!!! Ready Your To-Do List Application !!!")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. Exit")

def add_task():
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    tasks[task_name] = task_description
    print(f"Task '{task_name}' added successfully!")

def update_task():
    task_name = input("Enter task name to Update: ")
    if task_name in tasks:
        new_description = input("Enter new Description: ")
        tasks[task_name] = new_description
        print(f"Task '{task_name}' Updated successfully!")
    else:
        print(f"Task '{task_name}' not found.")

def delete_task():
    task_name = input("Enter The task name to delete: ")
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' Deleted successfully!")
    else:
        print(f"Task '{task_name}' not found.")

def view_tasks():
    if tasks:
        print("\n!!! Tasks !!!")
        for task_name, task_description in tasks.items():
            print(f"{task_name}: {task_description}")
    else:
        print("Tasks No Found.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        update_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        view_tasks()
    elif choice == '5':
        print("Exiting program!! Thank You!!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5")
