# Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name" и "email", а значения для этих ключей будут браться с клавиатуры

final_dict: dict = {}
n = int(input('Введите число n: '))
final_dict = {n: {"name": input('Введите имя: '), "email": input('Введите email: ')} for n in range(n)}
print(final_dict)

