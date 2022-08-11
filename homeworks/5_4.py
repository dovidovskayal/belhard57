# Вводится строка, определить количество пар одинаковых символов рядом стоящих в строкt (не пересекающиеся вхождения)

text: str = input('Введите строку: ')
# a = 0
# for i in text:
  #  print(i)
   # print(text.index(i))
    #if text.index(i) == text.index(i):
        #a += 1
#print(text, '-', a)
i = 0
c = 0
while i < len(text) - 1:
    if text[i] == text[i+1]:
        c += 1
        i += 1
    i += 1
print(c)