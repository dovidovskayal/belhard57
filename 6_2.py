# Код Морзе для представления цифр и букв использует тире и точки.
# Напишите функцию для кодирования текстового сообщения в соответствии с кодом Морзе. (словари в помощь)
def morze (message):
    message_list = list(message)
    dict_lett = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-...',
        'e': '.',
        'f': '..-.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.---',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }
    for i in range(len(message_list)):
        message_list[i] = dict_lett.get(message_list[i],'значения нет')
    message = ''.join(message_list)
    return messege

message = input('Введите сообщение: ')
new_message = morze(message)
print(new_messege)

