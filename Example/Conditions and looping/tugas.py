# Task Manager
tasks = []

while True:
    # Display menu
    print("Task Manager Menu:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Add Task
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        # Delete Task
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("Current Tasks:")
            for index, task in enumerate(tasks):
                print(f"{index+1}. {task}")

            task_index = int(input("Enter the task number to delete: ")) - 1

            if task_index < 0 or task_index >= len(tasks):
                print("Invalid task number.")
            else:
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task}' deleted successfully!")

    elif choice == "3":
        # View Tasks
        if len(tasks) == 0:
            print("No tasks to display.")
        else:
            print("Current Tasks:")
            for index, task in enumerate(tasks):
                print(f"{index+1}. {task}")

    elif choice == "4":
        # Exit
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice. Please try again.")

print("Task Manager closed.")
