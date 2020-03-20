# list exercise
# No 1
listOne = [3, 6, 9, 12, 15, 18,21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()

oddelements = listOne[1::2]
print("Elements at odd index from listOne")
print(oddelements)

evenelements = listTwo[0::2]
print("Elements at even index from listTwo")
print(evenelements)

print("Final third list")
listThree.extend(oddelements)
listThree.extend(evenelements)
print(listThree)

# No 2
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list: ", sample_list)
element = sample_list.pop(4)
print("List after removing element at index 4: ", sample_list)

