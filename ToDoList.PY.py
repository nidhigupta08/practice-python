# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found")

# Function to print all tasks
def print_tasks():
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("No tasks added yet")

# Main function to interact with the user
def main():
    while True:
        print("\nTo-Do List Program")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            print_tasks()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
