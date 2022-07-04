# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

letters_dict ={}
text: str = input('Введите текст: ')
text_list: list = list(text)
text_list_len: int = len(text_list)
i =0
while i<=text_list_len-1:
    letters_dict[text_list[i]] = text_list.count(text_list[i])
    i+=1
print(letters_dict)
