def multiply(list_of_numbers):
    product = 1
    for number in list_of_numbers:
        product *=number
    return product


print("Product of numbers in a list is ",multiply((2,5,3,1,3,3,4)))