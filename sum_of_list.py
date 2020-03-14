def sum(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        total +=number
    return total


print("Sum of numbers in a list is ",sum((2,5,3,1,3,3,4,-56)))