import json

# Define an empty list to store tasks
tasks = []

# Function to load tasks from a file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

# Function to save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to add a task
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added:", task)

# Function to remove a task
def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print("Task removed:", removed_task["task"])
    else:
        print("Invalid task index")

# Function to mark a task as completed
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed:", tasks[task_index]["task"])
    else:
        print("Invalid task index")

# Function to print all tasks
def print_tasks():
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, 1):
            status = " [X]" if task["completed"] else " [ ]"
            print(f"{index}.{status} {task['task']}")
    else:
        print("No tasks added yet")

# Main function to interact with the user
def main():
    load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            print_tasks()
            task_index = int(input("Enter the task index to remove: ")) - 1
            remove_task(task_index)
        elif choice == "3":
            print_tasks()
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            complete_task(task_index)
        elif choice == "4":
            print_tasks()
        elif choice == "5":
            save_tasks()
            print("Tasks saved. Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
