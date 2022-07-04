# Заполнить словарь где ключами будут выступать числа от 0 до n,
# а значениями вложенный словарь с ключами "name" и "email", а значения для этих ключей будут браться с клавиатуры

final_dict: dict = {}
n = int(input('Введите число n: '))
i = 0
while i<=n-1:
    name_email_dict: dict = {}
    name = input('Введите имя: ')
    name_email_dict['name'] = name
    email = input('Введите свой email: ')
    name_email_dict['email'] = email
    final_dict[i] = name_email_dict
    i+=1
print(final_dict)

