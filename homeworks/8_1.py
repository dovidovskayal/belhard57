while True:
    some_lst = [1, 2, 3, 4, 5, 6, 7]
    a = input('Введите < или >: ')
    i = 0
    print(some_lst[i])
    if a == ">":
         i+=1
    if a == '<':
        i-=1
    if i == -1:
        i = len(some_lst) - 1
    elif:
        i == len(some_lst)
        i = 0
   print(some_lst[i])
