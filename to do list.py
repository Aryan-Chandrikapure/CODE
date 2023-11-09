# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the to-do list
def add_task(task):
    tasks.append(task)
    print("Task added: " + task)

# Function to display the to-do list
def display_tasks():
    if len(tasks) == 0:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print("Task removed: " + removed_task)
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        task_index = int(input("Enter the index of the task to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")