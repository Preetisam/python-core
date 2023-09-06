# Create an empty to-do list as a Python list
to_do_list = []

# Add tasks to the list
task1 = {
    "name": "Buy groceries",
    "due_date": "2023-09-10",
    "priority": "High"
}

task2 = {
    "name": "Prepare presentation",
    "due_date": "2023-09-15",
    "priority": "Medium"
}

task3 = {
    "name": "Exercise",
    "due_date": "2023-09-07",
    "priority": "Low"
}

to_do_list.append(task1)
to_do_list.append(task2)
to_do_list.append(task3)

# Print the to-do list
print("Today's To-Do List:")
for task in to_do_list:
    print(f"Task: {task['name']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Priority: {task['priority']}")
    print("-" * 30)

# Modify a task
to_do_list[0]["priority"] = "Medium"

# Remove a task
to_do_list.pop(2)

# Updated To-Do List
print("\nUpdated To-Do List:")
for task in to_do_list:
    print(f"Task: {task['name']}")
    print(f"Due Date: {task['due_date']}")
    print(f"Priority: {task['priority']}")
    print("-" * 30)

