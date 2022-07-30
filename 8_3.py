# Бинарный поиск
n = int(input('Введите число '))
numbers = [1,2,3,4,5,6,7,8,9]
def binary_search(numbers, n):
    first = 0
    last = len(numbers) - 1
    i = 0
    while first <= last:
        mid = (first + last)//2
        s = numbers[mid]
        if n == s:
            return mid
        if n > s:
            first = mid + 1
        else:
            last = mid - 1
        i +=1
    return mid
print(binary_search(numbers, n))
