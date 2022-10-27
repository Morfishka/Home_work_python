# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

from random import randint

size = int(input('Введите длину последовательности: '))
numbers = [randint(1,size) for i in range(size)]
numbers_2 = list(set(numbers))

result = []
[result.append(i) for i in numbers if i not in result]

print(f"Начальная последовательность {numbers}")
print(f"Список из неповторяющихся элементов: {result}")
print(f"Последовательность без дубликатов {numbers_2}")
 