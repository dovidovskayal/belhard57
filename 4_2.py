# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

letters_dict ={}
text: str = input('Введите текст: ')
text_list: list = list(text)
n: int = len(text_list)
letters_dict = {text_list[i]: text_list.count(text_list[i]) for i in range(n)}
print(letters_dict)
