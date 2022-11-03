# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from math import factorial, prod

N = int(input("введите число: "))
# numbers = []
# for n in range(N):
#     numbers.append(n+1)
#     print(prod(numbers), end =' ')

# улучшение:

numbers = [n for n in range(1,N+1)]
numbers = list(map(lambda N: factorial(N), numbers))
print(numbers)

