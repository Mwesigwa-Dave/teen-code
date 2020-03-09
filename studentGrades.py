# 0 - 34 -> F9
# 35 - 44 -> P8
# 45 - 49 -> P7
# 50 - 54 -> C6
# 55 - 60 -> C5
# 60 - 64 -> C4
# 65 - 74 -> C3
# 74 - 79 -> D2
# 80 - 100 -> D1

# if (mark <= 34) {
#     print("F9")
# }

#list = [0,10,20,30,40,50,60,70,80,90,100]
#for mark in list:
#    print(mark)

def marks(list_of_marks):
    for mark in list_of_marks:
        if mark in range(0, 35):
            print("F9")
        elif mark in range(35, 45):
            print("P8")
        elif mark in range(45, 50):
            print("P7")
        elif mark in range(50, 55):
            print("C6")
        elif mark in range(55, 60):
            print("C5")
        elif mark in range(60, 65):
            print("C4")
        elif mark in range(65, 74):
            print("C3")
        elif mark in range(75, 80):
            print("D2")
        else:
            print("D1")

marks([12,75,93,29,41,74,67,44,89,21,47,76])