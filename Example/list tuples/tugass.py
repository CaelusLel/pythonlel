# Define a list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task, deadline):
    tasks.append((task, deadline))

# Function to display tasks based on priority and deadline
def display_tasks():
    # Sort tasks based on deadline (ascending order)
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    
    # Display tasks
    for task, deadline in sorted_tasks:
        print(f"Task: {task}, Deadline: {deadline}")

# Example usage
add_task("Task 1", "2022-01-01")
add_task("Task 2", "2022-01-05")
add_task("Task 3", "2022-01-03")

display_tasks()
