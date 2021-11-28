# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.'

# решение преподавателя
with open('HW52.txt') as file:
    file_lines = file.readlines()
    str_count = 0
    for num, line in enumerate(file_lines):
        str_count += 1
        words_count = len(line.split())
        print(f'#{num + 1} - {words_count} words')
    print(f'{str_count} strings')



# def calculations(file_path):
#
#     result = dict()
#     line_number = 0
#     try:
#         with open(file_path, 'r') as f:
#             for line_number, fl in enumerate(f, 1):
#                 result[line_number] = len(fl.split())
#     except Exception as err:
#         print(err)
#     return line_number, result


if __name__ == '__main__':
    num, counts = calculations('Lesson5/HW52.txt')
    print(f'Found {num} line(s)')
    for k, v in counts.items():
        print(f'Line {k}: {v} word(s)')




