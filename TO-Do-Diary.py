import os

def load_tasks():
    """
    Opening the Diary: Reads tasks from the file.
    Returns an empty list if the file doesn't exist.
    """
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        # strip() removes the newline character "\n" from each line
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """
    Writing into the Diary: Overwrites the file with the current list.
    """
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """
    Reading the List Out Loud: Prints all tasks with numbers.
    """
    if not tasks:
        print("\nYour To-Do list is empty.")
    else:
        print("\n--- YOUR TASKS ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("-" * 18)

def add_task(task, tasks):
    """
    Adding a New Entry: Appends to list and saves to file.
    """
    tasks.append(task)
    save_tasks(tasks)
    print(f"\nTask '{task}' added.")

def delete_task(index, tasks):
    """
    Crossing Off a Task: Removes item at specific index and saves.
    """
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"\nTask '{removed}' deleted.")
    else:
        print("\nInvalid task number.")

def main():
    """
    The Command Center: Controls the program flow.
    """
    tasks = load_tasks()
    
    while True:
        print("\n--- MENU ---")
        print("[1] Show Tasks")
        print("[2] Add Task")
        print("[3] Delete Task")
        print("[4] Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        
        elif choice == '2':
            new_task = input("Enter the task: ")
            add_task(new_task, tasks)
            
        elif choice == '3':
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                # Convert user input (1-based) to Python index (0-based)
                delete_task(task_num - 1, tasks)
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

# Only run the main function if this file is executed directly
if __name__ == "__main__":
    main()