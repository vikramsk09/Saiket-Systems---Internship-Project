# Create an empty list to store the tasks and their tasks
todo_list = []

def add_task():
    task = input("Enter the task to add: ")
    todo_list.append({"Task": task, "Status": "Pending"})
    print("New task added successfully!\n")

def view_task():
    print("Your to-do list: ")
    if len(todo_list) == 0:
        print("No Pending tasks.\n")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task["Task"]} - {task["Status"]}")
    print()

def remove_task():
    if len(todo_list) == 0:
        print("List is empty.\n")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task removed: {removed_task["Task"]}\n")
            else:
                print("Invalid Task number.\n")
        except ValueError:
            print("Please enter a valid Task number.\n")

def mark_done():
    if len(todo_list) == 0:
        print("List is empty.\n")
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as completed: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]["Status"] = "Done"
                print(f"Task - '{todo_list[search_index]["Task"]}' has been marked as done\n")
            else:
                print("Invalid Task number.\n")
        except ValueError:
            print("Please enter a valid Task number.\n")


# Function to display a Menu
def menu():
    while True:
        print("*** Main Menu ***")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application... Goodbye!")
            exit()
        else:
            print("Please choose a valid option.")

menu()

