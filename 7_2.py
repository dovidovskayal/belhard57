# Дано число, определить является ли оно простым

n: int = int(input('Enter number: '))
def prime_number(n):
    i = 10
    count = 0
    for i in range(2,n//2+1):
        if n == i:
            i -= 1
            continue
        if n%i == 0:
            print('No')
            count += 1
            i -= 1
    if count == 0:
        print('prime number')
    else:
        print('No')
prime_number(n)