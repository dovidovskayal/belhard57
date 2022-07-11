#Дан список содержащий в себе различные типы данных,
# отфильтровать таким образом, чтобы остались только строки, использование дополнительного списка незаконно
def onlystr(any_lst):
    any_lst = list(filter(lambda x: isinstance(x, str), any_lst))
    return any_lst

lst: list = ['hello', 3, (93, 5), 'python', [3, 'hell']]
a = onlystr(lst)
print(a)