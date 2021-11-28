# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
#


#решение от преподавателя

with open('HW51.txt', 'w') as file:
    input_line = input('Text: \n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line = input('Text: \n')

# мое решение

# my_list = []
# while True:
  #  lines = input("write something: ")
   # if lines == "":
   #     print(my_list)
   #     exit()
   # else:
   #     newline = lines + '  /n'
   #     my_list.append(newline)
   # with open(f"HW51.txt", "w+") as HW51:
   #     HW51.writelines(my_list)