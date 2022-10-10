# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


import re

number = input("Введите число: ")
number = re.sub('[!@#$+-,.]', '', number)
number = number.replace('-','')
numbers = []
for n in range(len(number)):
    numbers.append(int(number[n]))
print(sum(numbers))