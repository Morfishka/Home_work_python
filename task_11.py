# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from itertools import count
from os import remove


lst = [4, 6, 4, 3, 2, 1, 9, 5]
# i = 1
# sum = 0
# while i < len(lst):
#     sum += lst[i]
#     i += 2
# print(sum)

# улучшение:

r = [lst[i] for i in range(len(lst)) if i % 2 == 1]
print(sum(r))



        