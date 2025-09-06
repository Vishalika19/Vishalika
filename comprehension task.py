# n=20
# l=[(i,i*i) for i in range(n) if i%2!=0]
# print(l)

# n=10
# d = {x: x**3 for x in range(1, 11)}
# print(d)


# s="programming in python"
# v="aeiou"
# set={i for i in s if i in v}
# print(set)

# d = {'a': 1, 'b': 2, 'c': 3}
# d1 = dict(zip(d.values(), d.keys()))
# print(d1)

# tuple = [(n, n*2, n*3) for n in range(1, 6)]
# print(tuple)


# num = [-3, -1, 0, 2, 4, -6]
# positives = [n for n in num if n > 0]
# print(positives)

# s = "Python makes coding easier"
# word_lengths = {word: len(word) for word in s.split()}
# print(word_lengths)


# list= ["Even" if n % 2 == 0 else "Odd" for n in range(1, 11)]
# print(list)

# tuple= tuple(n**2 for n in range(1, 8))
# print(tuple)


# nums = [1, 2, 2, 3, 4, 4, 5, 5, 6]
# new_sorted = sorted(set(nums))
# print(new_sorted)

# for row in range(5):
# for i in range(1, rows + 1):
#     print(" " * (rows - i) * 2 + "* " * i)
#     print(' ')


# rows=5
# for i in range(rows, 0, -1):
#     print(" " * (rows - i) * 2 + "* " * i)
#     print(' ')


# rows = 5
# cols = 5
# for i in range(1, rows + 1):
#     for j in range(cols):
#         print(i, end=" ")
#     print()


# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# rows=5
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#hollow square
# rows=5
# for i in range(rows):
#     for j in range(rows):
#         if i==0 or i==rows-1 or j==0 or j==rows-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#rectangle of numbers(3*6)
# rows=3
# cols=6
# for i in range(rows):
#     for j in range(1,cols+1):
#         print(j,end=" ")
#     print()


# rows = 5
# for i in range(1,rows+1):
#     print(" "*(rows-i)+"* "*i)
#     print()

# rows=5
# for i in range(rows,0,-1):
#     print(" "*(rows-i)+"* "*i)
#     print()


#diamond pattern
rows=5
for i in range(1,rows+1):
    print(" "*(rows-i)+"* "*i)
for i in range(rows-1,0,-1):
    print(" "*(rows-i)+"* "*i)
