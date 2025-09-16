import json
import os

# File to store tasks
FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks found!")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['title']} [{status}]")

# Main program
def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print("✅ Task added!")
        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to mark done: "))
                tasks[num-1]["done"] = True
                save_tasks(tasks)
                print("✔️ Task marked as done!")
            except:
                print("❌ Invalid choice")
        elif choice == "4":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                tasks.pop(num-1)
                save_tasks(tasks)
                print("🗑️ Task deleted!")
            except:
                print("❌ Invalid choice")
        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again!")

if __name__ == "__main__":
    main()
