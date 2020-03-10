temperature = int(input("Enter temperature: "))
print("Convert from 'F to C' or 'C to F'")
unit1 = input("From what unit: ")
unit2 = input("To what unit: ")
if unit1.upper() == "C" and unit2.upper == "F":
    fah = int((32/9) + (temperature/5))
    print(temperature,"C is ", fah, " in fahrenheit")
elif unit1.upper() == "F" and unit2.upper() == "C":
    cel = int(5*(temperature - (32/9)))
    print(temperature,"F is ", cel, "in celcius")
else:
    print("Cannot change to the same unit")