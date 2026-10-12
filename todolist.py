
tasks = []

running = 1

while running == 1:
    print("1. Add an item")
    print("2. Delete an item at index")
    print("3. Remove the last item")
    print("4. Sort the list")
    print("5. Print the list")
    print("6. Exit the app")

    choice = int(input("Choose an option: "))

    if choice == 1:
        task = input("Enter a task (-1 to go back): ")

        while task != "-1":
            tasks.append(task)
            task = input("Enter a task (-1 to go back): ")

    elif choice == 2:
        print(tasks)
        index = int(input("Enter index: "))

        if index >= 0 and index < len(tasks):
            tasks.pop(index)
            print(tasks)
        else:
            print("Invalid index")

    elif choice == 3:
        if len(tasks) > 0:
            tasks.pop()
            print(tasks)
        else:
            print("List is empty")

    elif choice == 4:
        tasks.sort()
        print(tasks)

    elif choice == 5:
        print(tasks)

    elif choice == 6:
        running = 0
        print("Exit the app")

    else:
        print("Invalid option")
