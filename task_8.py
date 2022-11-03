# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите число: "))
# numbers = []
# for i in range(1, n+1):
#     numbers.append(round((1+1/i)**i, 2))
# print(numbers)
# print(f" сумма: {sum(numbers)}")

# улучшение:

numbers = [round((1+1/i)**i, 2) for i in range(1, n+1)]
print(numbers)
print(f" сумма: {sum(numbers)}")
