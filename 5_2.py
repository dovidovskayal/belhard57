# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
first_number: int = int(input('Введите первое число: '))
math_operation: str = input('Введите действие: ')
second_number: int = int(input('Введите второе число: '))
if math_operation == '+':
    result = first_number + second_number
elif math_operation == '-':
    result = first_number - second_number
elif math_operation == '*':
    result = first_number * second_number
elif math_operation == '/':
    result = first_number / second_number
elif math_operation == '%':
    result = first_number % second_number
elif math_operation == '**':
    result = first_number ** second_number
elif math_operation == '//':
    result = first_number // second_number
else:
    print('Такого действия нет')
print(first_number, math_operation, second_number, '=', result)
