# # Type of variables
# a = 5
# print(type(a))
#
# # Power: ** (double * operator)
# print(2 ** 3)  # =8
#
# # Area of circle
# pi = 3.14159
# radius = 2.2
# area = pi * (radius ** 2)
#
# # string concat
# hi = "Hello there"
# name = "Ana"
# greet = hi + " " + name
# print(greet)
#
# three_times = name * 3
# print(three_times)
#
# # variables conversion
# x = 5
# x_str = str(x)
# print("my favorite number is:", x)
# print("my favorite number is:" + " " + x_str)
#
# # input
# text = input("Type something... ")
# print(text * 5)
# number = int(input("Type a number..."))
# print(number * 5)
#
# # comparison
# x = float(input("x = "))
# y = float(input("y = "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("x / y =", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")
#
# # loops
# n = 0
# while n < 5:
#     print(n)
#     n = n + 1
#
# # scope
# x = 3
# def scope(x):
#     a = 4
#     x = x + 1
#     print(a)
#     print(x)
#
# scope(x)
#
# # tuple
# t = (2, 4, "a", 5)
# len(t)
#
# # lists
# L = [1, 2, 3, 4, "a", "b"]
# print(len(L))
# print(L[5])
# L.append(5)
# print(L)
# L1 = [3, 4, 5, 10]
# L2 = L + L1
# print(L2)
# L.extend([10, 11])  # works like append
# L.remove(2)  # removes the element with the value of 2
# del(L[2])  # delete the element with the index of 2
#
# # conversion
# s = "I<3 ds"
# print(list(s))
#
# sentence = "I love Python and Datascience"
# print(sentence.split(" "))
#
# L = ["P", "y", "th", "o", "n"]
# print(''.join(L))
