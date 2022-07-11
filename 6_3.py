# Дан список чисел и на вход поступает число N,
# необходимо сместить список на указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

def smeshenie(N, numbers_list):
    new_lst =[]
    for i in range(len(numbers_list)):
        if i < len(numbers_list) - N :
            print(i)
            new_lst.insert(i+N,numbers_list[i] )
        else:
            new_lst.insert(N-len(numbers_list)+i,numbers_list[i])
    return new_lst

N = int(input())
numbers_list = [1, 2, 3, 4, 5, 6, 7]
result_list = smeshenie(N, numbers_list)
print(result_list)