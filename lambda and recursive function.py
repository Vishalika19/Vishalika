# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def sum_n(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum_n(n-1)
# print(sum_n(5))

# def reverse_string(s):
#     if len(s)==0:
#         return s
#     else:
#         return s[-1]+reverse_string(s[:-1])
# print(reverse_string("vishalika"))

#recursive function to find the nth fibonacci number
# def fibonacci(n):
#     if n==0:
#         return n
#     elif n==1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# for i in range(10):
#     print(fibonacci(i),end=' ')

#recursive function to find sum of digits of a number
# def sum_of_digits(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sum_of_digits(n//10)
# print(sum_of_digits(1234))

#recursive function to calculate the power of a number(x^n)
# def power(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1 / power(x, -n)
#     return x * power(x, n - 1)
# print(power(2,2))

#lambda function to check if a number is even or odd
# check_even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
# print(check_even_odd(4))  
# print(check_even_odd(7))  

# max_num = lambda a, b: a if a > b else b
# print(max_num(5, 10))  
# print(max_num(12, 7)) 

# square = lambda x: x ** 2
# print(square(5))  
# print(square(9))  


# celsius = [0, 20, 30, 37, 100]
# fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
# print(fahrenheit)


# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)


data = [(1, 3), (2, 1), (4, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
