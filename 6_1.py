# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
def perevod(n):
    lst: list = []
    while n >= 1:
        k = n % 2
        lst.append(k)
        n = n // 2
    lst.reverse()
    str_list = ''.join(map(str, lst))
    return str_list


a = perevod(612)
print(a)
