
# решение преподавателя

with open("HW53.txt") as file:
    file_lines = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
average_sal = sum_salary / len(employees)
print(f'Average = {average_sal}')

for k, v in employees.items():
    if v < 20000:
        print(f'{k}: {v}')









# firm = {'Black': 40000, 'Smith': 60000, 'Potter': 15000, 'Green': 21000}
# try:
#     file_obj = open("Lesson5/HW53", 'w')
#     for last_name, salary in firm.items():
#         file_obj.write(last_name + ':' + str(salary) + "\n")
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     file_obj.close()
# summa = 0
# count = 0
# persons = []
# with open("Lesson5/HW53", "r") as file_obj:
#     for line in file_obj:
#         print(line, end="")
#         tokens = line.split(':')
#         if int(tokens[1]) <= 20000:
#            persons.append(tokens[0])
#         summa += int(tokens[1])
#         count += 1
# result = summa / count
# print(f"persons: {persons}")
# print(f"averate: {result}")







