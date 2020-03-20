# def my_name(name):
#     print("My name is ",name)

# my_name(Mwesigwa David)

# def args(*args):
#     total(args)
#     return total

    
# print(args(2,3,4,3,2,2))
dict = {"name":"Mwesigwa David", "age":19, "class":"university", "combination":"PEM/ict", "points":19}
# print(dict.keys())
# print(dict.values())
# for x,y in dict.items():
#     print(x,y) 
# for x in dict.values():
#     print(x)
# dict["name"] = "Davimpsalms"
# print(dict)
# print(pop(dict))
# creating a set
A = {"java", "Python", "C++", "PHP", "C"}
B = {1, 2, 3, 4, 5}
C = {"a", "b", "c", "d", "e"}
D = {"Mwesigwa", "David", "Musimenta", "Patricia", "Ahimbisibwe", "Julius", "Muwanguzi", "Jordan"}
E = {"Nakasi", "Grace", "Musimenta", "Nakitto", "Patricia", "David", "Alex"}
# for i in A:
#     print(i)
# print(set(C))
# print(A)
# A.add("Laravel")
# print(A)
# Adding more than one value in the set
A.update(["Nodejs", "CSS", "React"])
# print(A)
A.discard("java")
# # print(A)
# A.pop()
# print(A)
print(D&E)