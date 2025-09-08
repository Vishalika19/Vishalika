# lambda with single arguments
# # sq=lambda x:x*x
# print(sq(6))

#lambda with two args
# add=lambda a,b:a+b
# print(add(5,6))

#lambda with default args
# default=lambda x=10,b=20:x+b
# print(default())

#nested lambda
# mul1=lambda x: lambda y:x*y
# print(mul1(5)(6))

#lambda with no args
# name=lambda:"vishalika"
# print(name())

#factorial using Recursion
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(4))
    
#fibonocci using recursion
# def fib(n):
#     if n==0:
#         return n
#     elif n==1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(10):
#     print(fib(i),end=' ')


#sum of natural numbers
# def sumofnatural(n):
#     if n==0:
#         return 0
#     else:
#         return n+sumofnatural(n-1)
# print(sumofnatural(4))


#reverse of a string
# def rev(s):
#     if len(s)==0:
#         return s
#     else:
#         return s[-1]+rev(s[:-1])
# print(rev("vishalika"))

def revStr(string):
    if len(string)==0:
        return string
    else:
        return revStr(string[1:])+string[0]
print(revStr("vishalika"))


