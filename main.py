def show_menu():
    print("\n--- SMART TASK & TIME MANAGER ---")
    print("1. Add New Task")
    print("2. Start Task (Track Time)")
    print("3. View All Tasks")
    print("4. Save and Exit")
    print("---------------------------------")


def main():


    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            title = input("Enter task title: ")
            print(f"Task '{title}' created.")
            # Logic to add task will go here

        elif choice == '2':
            print("Fetching pending tasks...")
            # Logic to start timer will go here

        elif choice == '3':
            print("Displaying all tasks...")
            # Logic to show list will go here

        elif choice == '4':
            print("Saving data... Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()