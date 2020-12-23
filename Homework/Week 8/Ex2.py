list_1 = [1, 2, 3, 4, 6, 7, 8, 9, 20, 30]

list_1[2] = 0
print(list_1)

def multiple_verify(input_list, input_number):
    for element in input_list:
        if element % input_number == 0:
            return True
    return False

list_1 = [1, 2, 3, 4, 6, 7, 8, 9, 20, 30]
print(multiple_verify(list_1, 10))
print(multiple_verify(list_1, 6))
print(multiple_verify(list_1, 40))
