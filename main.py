my_str_1 = [1,2,3, 'hello', True, 5.6]
def my_type(element):
    for element in range(len(my_str_1)):
        print(type(my_str_1[element]))
    return
my_type(my_str_1)