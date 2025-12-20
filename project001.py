def tasks():

    todo_list = []

    print("Welcome to ToDo list......")

    total_tasks = int(input("How many tasks you want to do: "))

    for i in range(1, total_tasks + 1):
        task = input(f"Enter task {i}.... ")
        todo_list.append(task)

    print(f"Today tasks are {todo_list}")

    while True:

        choice = input(
            "Enter your choice!\n"
            "1_add\n"
            "2_update\n"
            "3_delete\n"
            "4_view\n"
            "5_exit\n"
        )

        if choice == "1":
            task = input("Enter task you want to add.... ")
            todo_list.append(task)
            print(f"Task '{task}' is successfully added.")

        elif choice == "2":
            task = input("Enter task you want to update: ")
            if task in todo_list:
                new_task = input("Enter new task: ")
                index = todo_list.index(task)
                todo_list[index] = new_task
                print(f"Task '{task}' successfully updated.")
            else:
                print("Task not found.")

        elif choice == "3":
            task = input("Enter the task you want to delete: ")
            if task in todo_list:
                todo_list.remove(task)
                print(f"Task '{task}' successfully deleted.")
            else:
                print("Task not found.")

        elif choice == "4":
            print(f"Your today tasks are: {todo_list}")

        elif choice == "5":
            print("Program is closing.....")
            break

        else:
            print("Invalid choice")


tasks()
