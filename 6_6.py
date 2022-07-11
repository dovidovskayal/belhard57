# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные
list_numbers = [1,3,2,6,64,3,14,8,65,9,56,11]
flist_numbers = list(filter(lambda x: x%2 == 0, list_numbers))
llist_numbers = list(filter(lambda x: x%2 != 0, list_numbers))
flist_numbers.extend(llist_numbers)
print(flist_numbers)