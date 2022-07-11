# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
def perevod(n):
    lst: list = []
    while n >= 1:
        k = n % 2
        lst.append(k)
        n = n // 2
    lst.reverse()
    str_list = ''.join(map(str, lst))
    list_two = [2**i for i in range(len(lst) - 1, 0, -1)]
    count = 0
    for i in range(len(lst)-1):
        a = lst[i]
        b = list_two[i]
        c = a * b
        print(c)
        count += c

    return str_list, count

some_number = int(input('Введите число: '))
a = perevod(some_number)
print(a)
