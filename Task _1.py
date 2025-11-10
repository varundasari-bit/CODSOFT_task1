tasks = []

def show_tasks():
    if tasks:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("\nTo-Do list is empty.")

def add_task():
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("Error: Please enter a task.")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task deleted: {removed}")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def modify_task():
    show_tasks()
    try:
        index = int(input("Enter the task number to modify: "))
        if 1 <= index <= len(tasks):
            new_task = input("Enter the new task description: ").strip()
            if new_task:
                old_task = tasks[index - 1]
                tasks[index - 1] = new_task
                print(f"Task updated: '{old_task}' → '{new_task}'")
            else:
                print("Error: Task description cannot be empty.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    while True:
        print("\n-----To-Do list-----")
        print("1. Add TASK")
        print("2. Show TASK")
        print("3. Delete TASK")
        print("4. Modify TASK")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            modify_task()
        elif choice == '5':
            print("DONE")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
