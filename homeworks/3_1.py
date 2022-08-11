# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
# Способ первый через .replace

user_sentence: str = input('Введите предложение: ')
user_sentence_new: str = user_sentence.replace(' ', '-')
print(user_sentence_new)


# Способ второй через .split и .join

user_sentence_split: str = user_sentence.split(' ')
user_sentence_join: str = '-'.join(user_sentence_split)
print(user_sentence_join)
