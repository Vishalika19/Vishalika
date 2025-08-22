# age=int(input("Enter your age:"))
# if age >= 18:
#     license = input(" Do you have license:")
#     if (license=='Yes'):
#         print("You can drrive")
#     else:
#         print("Go and get a license")
# else:
#     print("You are not eligible to dive")

# marks=int(input("Enter your marks:"))
# if marks>=35:
#     if marks>=90:
#         print(" you got o grade")
#     elif marks>=80:
#         print("You got A+ grade")
#     elif marks>=70:
#         print("You got A grade")
#     elif marks>=65:
#         print("You got D grade")
#     else:
#         print(" You got E grade")
# else:
#     print("you are fail")

# number=int(input("enter number:"))
# if number>0:
#     if number%2==0:
#         if number>=50:
#             print("Greater number")
#         else:
#             print("Smaller number")
#         print("Even number")
#     else:
#         print("Odd number")
#     print("Positive number")
# else:
#     print("Negative number")

age = int(input("enter age:"))
license=input("do you have license:")
if age>=18&(license=='Yes'):
    if age<18:
        print("you are minor")
    else:
        print(" you can drive after minor age")
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")
# age=int(input("enter age"))
# print('eligible to vote 'if age>=18 else' not eligible to vote')