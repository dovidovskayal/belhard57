# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные
list_numbers: list[int] = [1,3,2,6,64,3,14,8,65,9,56,11]
flist_numbers: list[int] = list(filter(lambda x: x%2 == 0, list_numbers))
llist_numbers: list[int] = list(filter(lambda x: x%2 != 0, list_numbers))
flist_numbers.extend(llist_numbers)
def sorted(numbers):
    i = 0
    while i<len(numbers):
        if not numbers[i]%2:
            numbers.insert(0,numbers.pop(i))
        else:
            i+=1
    return numbers
print(sorted(list_numbers))