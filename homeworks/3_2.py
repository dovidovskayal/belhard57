# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
# Делаем через функцию round

first_number: int = int(input('Введите первое число: '))
second_number: int = int(input('Введите второе число: '))
third_number: int = int(input('Введите третье число: '))
result: float = (first_number+second_number+third_number)/3
print(round(result, 3))
