tasks = []

while True:
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("Options:")
    print("1. Add Task")
    print("2. View List")
    print("3. Quit")

    choice = input("Enter choice (1/2/3):")

    if choice == '1':
        task = input("Enter a task: ")
        tasks.append(task)
    elif choice == '2':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Your To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == '3':
        break
    else:
        print("Invalid input")
