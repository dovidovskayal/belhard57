#Вывести первые N цисел кратные M и больше K

N = int(input('Введите число N: '))
M = int(input('Введите кратное число M: '))
K = int(input('Введите число K: '))
a = 1
for i in range(10000):
    if i % M == 0 and i > K and a <= N:
            a += 1
            print(i)
while N > 0:
    if K % M == 0:
        print(K)
        N -=1
    K += 1