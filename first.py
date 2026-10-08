marks = [10, 50, -5, 75]

totalSum = 0
count = len(marks)

for mark in marks:
    if mark < 0:
        continue
    totalSum += mark

print("Sum:", totalSum)
print("Total Students:", count)