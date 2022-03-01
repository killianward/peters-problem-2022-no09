# Peter's Problem 2022 No.9

from itertools import product

digit_to_list_dict = {
    0: [1, 1, 1, 0, 1, 1, 1],
    1: [0, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 1, 1, 0, 1],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 1, 0],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [0, 1, 0, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 1, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 0]}

four_zero_three = [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_list_version = []
new_binary_list = []
correct_prods = []
num_of_valid_nums = 0

def convert_to_binary_list(prod):
    binary_list_version.clear()
    for digit in prod:
        binary_list_version.append(digit_to_list_dict[digit])
    return binary_list_version

def correct_amnt_differences(binary_list):
    num_of_differences = 0
    num_of_lights = 0
    new_binary_list.clear()
    for list_ in binary_list:
        for item in list_:
            new_binary_list.append(item)
    
    for x, i in enumerate(new_binary_list):
        if i != four_zero_three[x]:
            num_of_differences += 1
        if i == 1:
            num_of_lights += 1
    
    if num_of_differences == 4 and num_of_lights == 15:
        return True
    else:
        return False


for prod in list(product(digits, repeat=3)):
    if correct_amnt_differences(convert_to_binary_list(prod)):
        num_of_valid_nums += 1
        correct_prods.append(prod)

print(f"\nAnswer: {num_of_valid_nums}\n\nCorrect Products: {correct_prods}")