from Methods import create_list_natural_numbers as create
from Methods import enter
from Methods import power_equation as equation

from Import_in_files import import_in_files as in_file

from random import randint
import os

os.system('cls')

max_power = enter('Введите максимально возможную степень в уравнении: ')
power = randint(1, max_power)
max_coeff = 100

coeffs = create (power + 1, max_coeff)
print(coeffs)
my_equation = equation(coeffs)
print(my_equation)

file = 'Power_equation.txt'
in_file (file, my_equation)