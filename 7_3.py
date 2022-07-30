# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером
# n х m,заполнив ее по спирали числами от 1 до n x m. Спираль начинается в левом верхнем углу
# и закручивается по часовой стрелке.
n: int = int(input('enter n: '))
m: int = int(input('enter m: '))
matrix = []
for i in range(0, m):
    matrix.append([])
    for j in range(1, n + 1):
        matrix[i].append(j)


def line_up(n, m, k, matrix):
    for i in range(0, n):
        matrix[0+k][i] = i + 1


def line_down(n, m, k, matrix):
    for i in range(n, 0, -1):
        matrix[m - 1 - k][i - 1 - k] = n + m + i - 2 - k
    matrix[m - 1 - k].reverse()


def line_right(n, m, k, matrix):
    for i in range(1, m - 1 - k):
        matrix[i][n - 1 - k] = n + i


def line_left(n, m, k matrix):
    for i in range(m - 2 - k, 0, -1):
        matrix[i][0+k] = n + m + n + m - 3 - i


while not m*n in matrix:
    line_up(n, m, matrix)
    line_down(n, m, matrix)
    line_right(n, m, matrix)
    line_left(n, m, matrix)
count = n + m - 2 + n + m - 2 + 1
while count <= n*m+1:
    k = 0
    k += 1
    for i in range(0 + k, n - k):
        matrix[k][i] = count
        count += 1
        print(k)
        print(count)
    if m > 4 and count <= n*m+1:
        for i in range(1 + k, m - 1 - k):
            matrix[i][n - 1 - k] = count
            count += 1
    if m > 3 and count <= n*m+1:
        for i in range(n - k, 0 + k, -1):
            matrix[m - 1 - k][i - k] = count
            count += 1
    if m > 4 and count <= n*m+1:
        for i in range(m - 2 - k, 0 + k, -1):
            matrix[i][0 + k] = count
            count += 1
print(matrix)
