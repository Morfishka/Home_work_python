# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

float_list = [2.4, 1.2, 5.8, 14.01]
# numbers = []
# for n in float_list:
#   if n % 1 != 0:
#     numbers.append(round(n % 1,2))
# result = max(numbers) - min(numbers)
# print(f'Разница между максимальным и минимальным значениями дробной части = {result}')


# улучшение:

numbers = [round(n % 1,2) for n in float_list if n % 1 != 0]
result = max(numbers) - min(numbers)
print(f'Разница между макс. и мин. значениями дробной части = {result}')
