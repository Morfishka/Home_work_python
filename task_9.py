# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


from math import prod

# N = int(input("введите число: "))

# array = []
# array_2 = []
# new_array = []
# for i in range(-N,N+1):
#     array.append(i)
# print(f'Диапазон элементов : {array}')

# text = open(r'D:\repo\Python_2block\Home_work_python\file.txt')

# for line in text:
#     array_2.append(int(line))
# print(f'Позиции элементов: {array_2}')

# for j in array_2:
#     new_array.append(array[j])

# print(f'Найденные элементы: {new_array}')
# print(f'Произведение найденных элементов: {prod(new_array)}')
# text.close()

# улучшение:

N = int(input("введите число: "))
text = open(r'D:\repo\Python_2block\Home_work_python\file.txt')
array = [i for i in range(-N,N+1)]
print(f'Диапазон элементов : {array}')
array_2 = [int(line) for line in text]
print(f'Позиции элементов: {array_2}')
new_array = [array[array_2[i]] for i in range(len(array_2))]
print(f'Найденные элементы: {new_array}')
print(f'Произведение найденных элементов: {prod(new_array)}')
text.close() 