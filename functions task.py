# def cube(n):
#     return n ** 3
# print(cube(4))


# def average(a, b):
#     return (a + b) / 2
# print(average(10, 20)) 


# def is_odd(n):
#     return n % 2 != 0
# print(is_odd(7))  
# print(is_odd(8))  

# def sum_digits(n):
#     return sum(int(digit) for digit in str(n))
# print(sum_digits(1234))

# def greet(name='Guest'):
#     return f"Hello, {name}"
# print(greet())       
# print(greet("Vishalika"))  

# def power(base, exponent=2):
#     return base ** exponent
# print(power(5))       
# print(power(2, 3))    

# def total_bill(item='Sandwich', quantity=1, price=50):
#     return quantity * price
# print(total_bill())                  
# print(total_bill('Pizza', 3, 120))  

# def employee_info(name, age=30, department='HR'):
#     return f"Name: {name}, Age: {age}, Department: {department}"
# print(employee_info("Alice"))      
# print(employee_info("Bob", 25, "IT"))

# def circle_area(radius=1):
#     return 3.14 * radius * radius
# print(circle_area())       
# print(circle_area(5))  

# def sum_even(n):
#     total = 0
#     for i in range(2, n+1, 2):
#         total += i
#     return total
# print(sum_even(10))  
    
# def largest_number(numbers):
#     return max(numbers)
# print(largest_number([10, 25, 5, 40]))


# def min_max(numbers):
#     return min(numbers), max(numbers)
# minimum, maximum = min_max([5, 12, 3, 20])
# print("Min:", minimum, "Max:", maximum)

# def student_summary(name, marks):
#     total_marks = sum(marks)
#     average_marks = total_marks / len(marks)
#     return name, total_marks, average_marks
# name, total, avg = student_summary("Vishalika", [80, 90, 70])
# print(f"Name: {name}, Total: {total}, Average: {avg:.2f}")


def calculate(num1, num2, operator='add'):
    if operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2
    elif operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
print(calculate(10, 5))                 
print(calculate(10, 5, 'subtract'))     
print(calculate(10, 5, 'multiply'))     
print(calculate(10, 5, 'divide'))       
print(calculate(10, 0, 'divide'))       