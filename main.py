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
digits = [0, 1]
indices_of_digit1 = [0, 1, 2, 3, 4, 5, 6]
indices_of_digit2 = [7, 8, 9, 10, 11, 12, 13]
indices_of_digit3 = [14, 15, 16, 17, 18, 19, 20]
digit1 = []
digit2 = []
digit3 = []
num_of_valid_nums = 0

def check_for_amnt_of_differences(prod):
    print(type(prod))
    count = 0
    for x, digit in prod:
        if not digit == four_zero_three[x]:
            count += 1
    if count == 2:
        return True

def check_if_valid_num(digit1, digit2, digit3):
    condition1 = False
    condition2 = False
    condition3 = False
    for num in digit_to_list_dict:
        if num == digit1:
            condition1 = True
        if num == digit2:
            condition2 = True
        if num == digit3:
            condition3 = True
    
    if condition1 and condition2 and condition3:
        return True


for prod in list(product(digits, repeat=21)):
    if check_for_amnt_of_differences(prod):
        for x, digit in enumerate(prod):
            if x in indices_of_digit1:
                digit1.append(digit)
            if x in indices_of_digit2:
                digit2.append(digit)
            if x in indices_of_digit3:
                digit3.append(digit)
        
        if check_if_valid_num(digit1, digit2, digit3):
            num_of_valid_nums += 1

print(num_of_valid_nums)
