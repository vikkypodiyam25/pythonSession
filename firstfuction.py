# # # # # # # 

# # # # # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # # # # # for i in range(2, 6):
# # # # # #     print(numbers[i])
    
    
# # # # # # # numbers = [1,2,3,4,5,6,7,8,9,10]

# # # # # # # start = int(input("Enter start: "))
# # # # # # # end = int(input("Enter end: "))

# # # # # # # for i in range(start, end + 1):
# # # # # # #     print(numbers[i])


# # # # # tasks = []

# # # # # running = 1

# # # # # while running == 1:
# # # # #     print("1. Add task")
# # # # #     print("2. Delete task")
# # # # #     print("3. Remove last task")
# # # # #     print("4. Sort list")
# # # # #     print("5. Show list")
# # # # #     print("6. Exit")

# # # # #     choice = int(input("Enter choice: "))

# # # # #     if choice == 1:
# # # # #         task = input("Enter task: ")

# # # # #         while task != "-1":
# # # # #             tasks.append(task)
# # # # #             task = input("Enter task: ")

# # # # #     elif choice == 2:
# # # # #         index = int(input("Enter index: "))
# # # # #         if index >= 0 and index < len(tasks):
# # # # #             tasks.pop(index)
# # # # #         print(tasks)

# # # # #     elif choice == 3:
# # # # #         if len(tasks) > 0:
# # # # #             tasks.pop()
# # # # #         print(tasks)

# # # # #     elif choice == 4:
# # # # #         tasks.sort()
# # # # #         print(tasks)

# # # # #     elif choice == 5:
# # # # #         print(tasks)

# # # # #     elif choice == 6:
# # # # #         running = 0

# # # # # print("Exit")


# # # # student = ("Rahul", 101, "A")
# # # # print(student[1], student[0], student[2])


# add the value in list
# t1 = (1, 2)
# temp = list(t1)
# temp.extend([8, 11])
# t1 = tuple(temp)
# print(t1)


# # # write a lamda call is_passing that wiill return true if marks >40

# # passing = lambda marks: marks > 40
# # print(passing(75))  
# # print(passing(40))  
# # print(passing(25))  





# How to query sorted in lambda
# items = [("Zucchini", 40), ("Banana", 100), ("Apple", 25)]
# sorted_items = sorted(items, key=lambda item: item[0].lower())
# print(sorted_items)


# change the muteable means change the value
# cities = (["mumbai", 5000], ["hyd", 1000], ["DW", 50])
# cities[0][0] = "delhi"
# print(cities)



words = ["apple", "banana", "elephant", "cat"]

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)