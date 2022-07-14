# Код Морзе для представления цифр и букв использует тире и точки.
# Напишите функцию для кодирования текстового сообщения в соответствии с кодом Морзе. (словари в помощь)
def morze(message):
    #message_list = list(message)
    dict_lett: dict = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-...',
        'e': '.',
        'f': '..-.',
        'g': '--.',
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
        ' ': '  ',
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
    #for i in range(len(message_list)):
     #  message_list[i] = dict_lett.get(message_list[i], 'значения нет')
    #message = ''.join(message_list)
    #return message
    morze_message = ''
    for letter in message.lower():
        if letter in dict_lett:
            morze_message +=dict_lett[letter]
    return (morze_message)

message: str = input('Введите сообщение: ')
new_message: str = morze(message.lower())
print(new_message)
