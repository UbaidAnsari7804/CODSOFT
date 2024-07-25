import json
import os

# Define the path for the todo list file
todo_file = 'todo_list.json'

# Load the existing to-do list from the file, if it exists
def load_todo_list():
    if os.path.exists(todo_file):
        with open(todo_file, 'r') as file:
            return json.load(file)
    return []

# Save the current to-do list to the file
def save_todo_list(todo_list):
    with open(todo_file, 'w') as file:
        json.dump(todo_list, file, indent=4)

# Display the to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            status = "Done" if task["done"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

# Add a new task to the to-do list
def add_task(todo_list):
    task = input("Enter the new task: ")
    todo_list.append({"task": task, "done": False})
    save_todo_list(todo_list)
    print("Task added.")

# Update an existing task in the to-do list
def update_task(todo_list):
    display_todo_list(todo_list)
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(todo_list):
        new_task = input("Enter the updated task: ")
        todo_list[task_num]["task"] = new_task
        save_todo_list(todo_list)
        print("Task updated.")
    else:
        print("Invalid task number.")

# Mark a task as done
def mark_task_done(todo_list):
    display_todo_list(todo_list)
    task_num = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_num < len(todo_list):
        todo_list[task_num]["done"] = True
        save_todo_list(todo_list)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

# Delete a task from the to-do list
def delete_task(todo_list):
    display_todo_list(todo_list)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(todo_list):
        todo_list.pop(task_num)
        save_todo_list(todo_list)
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Main function to run the to-do list application
def main():
    todo_list = load_todo_list()
    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            update_task(todo_list)
        elif choice == '4':
            mark_task_done(todo_list)
        elif choice == '5':
            delete_task(todo_list)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
