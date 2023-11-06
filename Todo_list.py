todo_list = []

while True:
    task = input("Enter a task (or 'quit' to exit): ")
    if task == 'quit':
        break
    todo_list.append(task)

print("Your To-Do List:")
for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")
