# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))

def multi(n):
    res = [i for i in range(2, n)]
    res = list(filter(lambda i : n % i == 0, res))
    print(res)
        
multi(n)
