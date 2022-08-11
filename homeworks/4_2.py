# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

letters_dict ={}
text: str = input('Введите текст: ')
n: int = len(text)
letters_dict: dict = {text[i]: text.count(text[i]) for i in range(n)}
print(letters_dict)
