from random import randint

def enter (message):
    num = int(input(message))
    return num

def create_list_natural_numbers (length, max):
    nat_nums = []
    for i in range (length):
        nat_nums.append(randint(0, max))
    return nat_nums

def power_equation (coeffs):
    equation = ''
    for i in range (len(coeffs) - 1, 0, -1):
        if coeffs[i] != 0:
            if i == 1:
                equation += f'{coeffs[i]}x + '
            else:
                equation += f'{coeffs[i]}x^{i} + '
    if coeffs[i] == 0:
        equation += ' = 0'
    else:
        equation += f'{coeffs[0]} = 0'
    return equation