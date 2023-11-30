
# Initialize an empty queue
queue = []

# Set the maximum number of people in the queue
max_people = 5

# Start the simulation
while True:
    # Check if the queue is full
    if len(queue) >= max_people:
        print("The queue is full. No more people can join.")
        break

    # Prompt the user to enter a name
    name = input("Enter a name (or 'q' to quit): ")

    # Check if the user wants to quit
    if name == 'q':
        print("Quitting the simulation.")
        break

    # Add the name to the queue
    queue.append(name)
    print(f"{name} has joined the queue.")

# Print the final queue
print("Final queue:")
for person in queue:
    print(person)
