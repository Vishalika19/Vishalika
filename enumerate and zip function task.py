# fruits=["apple","banana","cherry"]
# for index,fruit in enumerate(fruits):
#     print(index,' ',fruit)


# students=["Alice","Bob","Charlie"]
# for index,student in enumerate(students,start=1):
#     print(index,' ',student)

# colors=["red","green","blue"]
# for index,color in enumerate(colors):
#     print(index,' ',color)

# languages=["java","c++","python","ruby"]
# for index,language in enumerate(languages):
#     if language == "python":
#         print("Index of 'python' is:", index)

# str="hello"
# for index,char in enumerate(str):
#     print(index,' ',char)
    
# names = ["Alice", "Bob", "Charlie"]
# marks = [85, 90, 78]
# list = list(zip(names, marks))
# print(list)


# names = ["Alice", "Bob", "Charlie"]
# marks = [85, 90, 78]
# for name, mark in zip(names, marks):
#     print(f"{name} scored {mark}")

# pairs = [("a", 1), ("b", 2), ("c", 3)]
# keys, values = zip(*pairs)
# print("Keys:", keys)
# print("Values:", values)

# ids = [101, 102, 103]
# names = ["Tom", "Jerry", "Mickey"]
# grades = ["A", "B", "A"]
# for student in zip(ids, names, grades):
#     print(student)

a = [1, 2, 3, 4]
b = ["x", "y"]
result = list(zip(a, b))
print(result)

