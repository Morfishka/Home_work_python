# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

array = [6, 6, 4, 1, 2]

def prod_pair_of_numbers(list):
    prod_result = []
    i = 1
    while i <= len(list)/2:
        prod_result.append(list[i-1]*list[i*(-1)])
        i += 1
    if len(list) % 2 != 0:
        prod_result.append(list[len(list)//2]**2)
    return prod_result

print(prod_pair_of_numbers(array))