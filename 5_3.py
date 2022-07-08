# Вывести четные числа от 2 до N по 5 в строку

N: int = int(input())
some_lst: list[int] = [i for i in range(2, N + 1) if i % 2 == 0]
for i in some_lst:
    a: int = some_lst.index(i) + 1
    if not a % 5 == 0 or a == 0:
        print(i, end=' ')
    else:
        print(i, end='\n')



c = 0
for i in range(2, N+1,2):
    if c<5:
        print(i, end=' ')
        c +=1
    else:
        c =1
        print()
        print(i,end=' ')



