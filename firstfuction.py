# def calculate_total(price, quantity):
#     total = price * quantity
#     print("Total Amount:", total)

# p1 = float(input("Price daalein: "))
# q1 = int(input("Quantity daalein: "))
# calculate_total(p1, q1)

# calculate_total(50, 3)


def calculate_fine(days, book_type="standard", is_premium=False):
    
    if book_type == "reference":
        fine = days * 20

    elif days <= 5:
        fine = days * 5

    else:
        fine = 25 + (days - 5) * 10

    if is_premium:
        fine = fine * 0.8

    return fine

print("Standard, 3 days, Regular:", calculate_fine(3))  
print("Standard, 7 days, Regular:", calculate_fine(7))        
print("Reference, 4 days, Regular:", calculate_fine(4, "Reference"))
print("Standard, 10 days, Premium:", calculate_fine(10, "Standard", True))
