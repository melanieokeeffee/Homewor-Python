from functools import reduce

# четные
num_set = {i for i in range(100, 1001) if i % 2 ==0}
print(num_set)

# перемножение
summ = reduce((lambda x, y: x * y), num_set)
print(summ)








