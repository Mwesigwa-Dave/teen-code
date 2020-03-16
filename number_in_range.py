def check_in_range(n):
    if n in range(2, 23):
        print("%s is in the range"%str(n))
    else:
        print("%s not in range"%str(n))

n = int(input("Enter number to be checked: "))
check_in_range(n)