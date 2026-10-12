# # 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(2, 6):
#     print(numbers[i])
    
    
# # numbers = [1,2,3,4,5,6,7,8,9,10]

# # start = int(input("Enter start: "))
# # end = int(input("Enter end: "))

# # for i in range(start, end + 1):
# #     print(numbers[i])


tasks = []

running = 1

while running == 1:
    print("1. Add task")
    print("2. Delete task")
    print("3. Remove last task")
    print("4. Sort list")
    print("5. Show list")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")

        while task != "-1":
            tasks.append(task)
            task = input("Enter task: ")

    elif choice == 2:
        index = int(input("Enter index: "))
        if index >= 0 and index < len(tasks):
            tasks.pop(index)
        print(tasks)

    elif choice == 3:
        if len(tasks) > 0:
            tasks.pop()
        print(tasks)

    elif choice == 4:
        tasks.sort()
        print(tasks)

    elif choice == 5:
        print(tasks)

    elif choice == 6:
        running = 0

print("Exit")
