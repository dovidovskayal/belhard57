# Найти 2 5значных делителя числа
# 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139

n = '1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139'
a = []
b = []
for i in range(0,len(n)-1,5):
    a.append(n[i:i+5])
for i in range(10000, 100000):
    ost = 0
    for j in range(0, len(a)-1):
        delit = int(str(ost)+ a[j])
        ost = delit%i
        b.append((delit) // i)

print(b)




# деление в столбик реализовать