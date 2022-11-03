# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

array = [6, 5, 4, 1, 3]

# def prod_pair_of_numbers(lst):
    # prod_result = []
    # i = 1
    # while i <= len(list)/2:
    #     prod_result.append(list[i-1]*list[i*(-1)])
    #     i += 1
    # if len(list) % 2 != 0:
    #     prod_result.append(list[len(list)//2]**2)

#     return prod_result

# print(prod_pair_of_numbers(array))

# улучшение:

def prod_pair_of_numbers(lst):

    prod_result = [lst[i]*lst[len(lst)-i-1] for i in range(len(lst)//2)]
    if len(lst) % 2 != 0:
        prod_result.append(lst[len(lst)//2]**2)
    return prod_result

print(prod_pair_of_numbers(array))