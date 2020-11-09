# import time
#
# def c_to_f(x):
#     return x * 9 / 5 + 32
#
# t0 = time.perf_counter()
# c_to_f(100000)
# t1 = time.perf_counter()
# print("Time is:", t1 - t0)
#
# def mysum(x):
#     total = 0
#     for i in range(x + 1):
#         total = total + 1
#     return total
#
# print(mysum(10))
#
#
# def search_for_elem(list1, elem):
#     for i in list1:
#         if i == elem:
#             return True
#     return False
#
# List1 = [1, 2, 3, 4, 5]
# print(search_for_elem(List1, 1))
# print(search_for_elem(List1, 8))
#
#
# def fact_iter(n):
#     answer = 1
#     while n > 1:
#         answer *= n
#         n -= 1
#     return answer
