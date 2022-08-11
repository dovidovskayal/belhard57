# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
# Первый способ через %-форматирование

user_name: str = input('Введите Ваше имя: ')
user_age: int = int(input('Введите Ваш возраст: '))
user_city: str = input('Введите Ваш город: ')
message_first = 'Привет, %s! Твой возраст %d и ты из города %s, так?'%(user_name, user_age, user_city)
print(message_first)
# Второй способ через метод format()
message_second= 'Привет, {}! Твой возраст {} и ты из города {}, так?'.format(user_name, user_age, user_city)
print(message_second)
# Третий способ через f-строки
message_third= f'Привет, {user_name}! Твой возраст {user_age} и ты из города {user_city}, так?'
print(message_third)


