# Дан список чисел, необходимо его развернуть без использования метода revese и функции reversed,
# а так же дополнительного списка и среза
def foo(lst):
    for i in range(len(lst)//2):
        temp = lst[i]
        lst[i] = lst[-i-1]
        lst[-i-1] = temp
    return lst
numbers_lst = [1,2,3,4,5,6,7,8,9]
a = foo(numbers_lst)
print(a)