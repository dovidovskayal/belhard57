# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

first_number: int = int(input('Введите первое число: '))
second_number: int = int(input('Введите второе число: '))
third_number: int = int(input('Введите третье число: '))
first_number_res: bool = first_number > 0
second_number_res: bool = second_number > 0
third_number_res: bool = third_number > 0
positive_result: int = first_number_res + second_number_res + third_number_res
print('Положительных чисел: ', positive_result)
print('Отрицательных чисел: ', 3 - positive_result)