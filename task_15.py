# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = abs(int(input("Введите число: ")))
numbers = [1,1]
numbers2 = []
for i in range(2, n):
    numbers.append(numbers[-1] + numbers[-2])
for i in range(n):
    numbers2.insert(0,numbers[i]*-1)
print(numbers2 + numbers, end =' ')
