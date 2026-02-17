def main():
    tasks = []
    print("--- Simple Python Task Manager ---")

    while True:
        print("\nOptions: [1] Add Task [2] Show Tasks [3] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print("Task added!")
        elif choice == "2":
            print("\nYour To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()