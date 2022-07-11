# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение - словарь с данными о пользователе
# (имя, фамилия, телефон, почта), вывести имена тех, у кого не указана почта
# (нет ключа email или значение этого ключа - пустая строка)

users: dict = {
    1: {
        'name': 'Alex',
        'last name': 'Petrov',
        'phone': '154567'

    },
    2:{
        'name': 'Fedya',
        'last name': 'kuskov',
        'phone': '1308539',
        'email': 'kusok@mail.com'

    },
    3: {
        'name': 'Nadya',
        'last name': 'Kukuruzkina',
        'phone':'9434567',
        'email':''

    },
    4: {
        'name': 'Gulya',
        'last name': 'Kavkazova',
        'phone': '067565486',
        'email': 'gorniy@mail.com'

    }
}
for user in users.values():
    if 'email' not in user or not user['email']:
        print(user['name'])