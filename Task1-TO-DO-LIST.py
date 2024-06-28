def display_menu():
    print("\n-------------Welcome To The TO-DO List Management App---------------")
    print("Press 1 to Add a New Task")
    print("Press 2 to Update a Task")
    print("Press 3 to Delete a Task")
    print("Press 4 to View All Tasks")
    print("Press 5 to Exit and Stop")

def add_task(tasks, total_task):
    remaining_tasks = total_task - len(tasks)
    if remaining_tasks <= 0:
        print(f"You have set the task limit {total_task} for the day, Now You are exeeding it please delete previous task to add new task")
        return

    num_new_tasks = int(input(f"How many tasks would you like to add? (up to {remaining_tasks}): "))
    if num_new_tasks > remaining_tasks:
        print(f"You can only add up to {remaining_tasks} more tasks.")
        return

    for i in range(len(tasks) + 1, len(tasks) + num_new_tasks + 1):
        task_name = input(f"Enter task {i}: ").lower()
        priority = input("Enter the priority (high, medium, low): ").lower()
        status = input("Enter the status (pending, completed, in progress): ").lower()
        tasks.append({'name': task_name, 'priority': priority, 'status': status})
        print(f"Task '{task_name}' with priority '{priority}' and status '{status}' has been successfully added.")

def delete_task(tasks):
    task_name = input("Enter the task name you want to delete: ").lower()
    for task in tasks:
        if task['name'] == task_name:
            tasks.remove(task)
            print(f"Task '{task_name}' has been deleted.")
            return
    print(f"Task '{task_name}' not found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Current Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"Task {i}: Name: {task['name']}, Priority: {task['priority']}, Status: {task['status']}")

def update_task(tasks):
    task_name = input("Enter the task name you want to update: ").lower()
    for task in tasks:
        if task['name'] == task_name:
            new_name = input("Enter the new name (leave blank to keep current name): ").lower()
            new_priority = input("Enter the new priority (high, medium, low) (leave blank to keep current priority): ").lower()
            new_status = input("Enter the new status (pending, completed, in progress) (leave blank to keep current status): ").lower()

            if new_name:
                task['name'] = new_name
            if new_priority:
                task['priority'] = new_priority
            if new_status:
                task['status'] = new_status

            print(f"Task '{task_name}' has been updated to Name: '{task['name']}', Priority: '{task['priority']}', Status: '{task['status']}'")
            return
    print(f"Task '{task_name}' not found.")

def main():
    tasks = []
    total_task = int(input("Enter the total number of tasks you want to set for the day: "))
    initial_tasks = int(input(f"Enter how many tasks you want to add initially (up to {total_task}): "))

    for i in range(1, initial_tasks + 1):
        task_name = input(f"Enter task {i}: ").lower()
        priority = input("Enter the priority (high, medium, low): ").lower()
        status = input("Enter the status (pending, completed, in progress): ").lower()
        tasks.append({'name': task_name, 'priority': priority, 'status': status})
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task(tasks, total_task)
            elif choice == 2:
                update_task(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                view_tasks(tasks)
            elif choice == 5:
                print("Closing the program...")
                break
            else:
                print("Invalid input. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

main()
