# Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних чисел одним из соседей является число с противоположной стороны списка
def foo(lst):
    #for i in range(len(lst)):
        #if i < len(lst) - 1:
           # print('Для элемента', i, ':', lst[i-1], '+', lst[i+1], '=', lst[i-1]+lst[i+1])
       # else:
            #print('Для элемента', i, ':', lst[i-1], '+', lst[-i+1], '=', lst[i-1]+lst[-i+1])
    neighbour = []
    for i in range(len(lst)):
        if i == len(lst)-1:
            neighbour.append(lst[i-1] + lst[0])
        else:
            neighbour.append(lst[i-1] + lst[i+1])
    return neighbour

some_list: list[int] = [12,13,11,22,24]
foo(foo(some_list))
