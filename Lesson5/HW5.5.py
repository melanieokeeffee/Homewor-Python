# -*- coding: utf8 -*-
# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

# решение преподавателя
import random
with open('HW55.txt', 'w') as file:
    for _ in range(30):
        file.write(f'{random.randint(0, 10)} ')

with open('HW55.txt') as file:
    nums_str = file.read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)
print(sum)


# with open('HW55.txt', 'w+') as HW55:
#     line = input('Введите цифры через пробел \n')
#     HW55.writelines(line)
#     my_numb = line.split()
#
#     print(sum(map(int, my_numb)))
