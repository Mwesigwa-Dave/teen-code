def case_check(string):
    d = {"UPPER_CASE":0, "LOWER_CASE":0}
    for c in string:
        if c.isupper():
            d["UPPER_CASE"] +=1
        elif c.islower():
            d["LOWER_CASE"] +=1
        else:
            pass
    print("Original string is ",string,)
    print("No. of upper case characters: ",d["UPPER_CASE"])
    print("No. of lower case characters: ",d["LOWER_CASE"])


case_check("Teen Code Kampala")