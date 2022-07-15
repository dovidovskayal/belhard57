# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером
# n х m,заполнив ее по спирали числами от 1 до n x m. Спираль начинается в левом верхнем углу
# и закручивается по часовой стрелке.
n: int = int(input('enter n: '))
m: int = int(input('enter m: '))
matrix = []
for i in range(0, m):
    matrix.append([])
    a = n
    while len(matrix[i]) < a:
        for d in range(1,n+1):
                matrix[i].append(d)
                a -= 1

matrix[m//2][n//2] = n*m

print(matrix)
