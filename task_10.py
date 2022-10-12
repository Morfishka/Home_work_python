# Реализуйте алгоритм перемешивания списка.

import random

list = [6, 4, 16, 7, 4, 5]
print(f'Исходный список: {list}')
print(f"Перемешанный список: {random.sample(list,len(list))}")

# or:

for n in range(len(list)-1,0,-1):
    i = random.randint(0, n)
    list[n],list[i] = list[i],list[n]
print(f'второй способ перемешивания: {list}')