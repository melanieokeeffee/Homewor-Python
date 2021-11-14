# # тяжело было решить этот номер, опиралась на решене другого человека
# # поэтому прописываю мнго комментариев, чтобы было видноб что списывала не безбумно
#
# # строим функцию, задача которой вычисление суммы
# # вводимых чисел в пределах 1 ввода пользователем
def my_sum():
    sum_res = 0
    str1 = False
    while str1 == False:
        # нужно показать фунции что складывать нужно числа разделенные пробелом
        number = input('Input numbers ').split()

        result = 0
        for el in range(len(number)):
            # Чтобы остановить цикл  нужно написать значение при котором будет выход из цикла
            if number[el] == 'q' or number[el] == 'Q':
                str1 = True
                break
            else:
                # получаем сумму получаемых вводных данных
                result = result + int(number[el])
        #сумма результата+ новых вводных
        sum_res = sum_res + result
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')
my_sum()