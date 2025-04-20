import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Show tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done." if task["done"] else "Not Done."
            print(f"{i}. [{status}] {task['task']}")

# Add task
def add_task(tasks):
    task_text = input("Enter the task: ")
    tasks.append({"task": task_text, "done": False})
    print("Task added.")

# Delete task
def delete_task(tasks):
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark task as done
def mark_done(tasks):
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
