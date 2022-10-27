# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

data  = open('polynomial.txt','w')

k = int(input("Введите степень k: "))
coeff = [randint(0,100) for i in range(k + 1)]
print(coeff)

result = ''
j = len(coeff)-1
while j > 0:
    for i in range(len(coeff)):
        if len(result) > 0 and coeff[i] > 0:
            result += ' + '
        if j == 1:
            result += str(coeff[i]) + 'x'
            j -= 1
        elif coeff[i] == 1:
            result += 'x^' + str(j)
            j -= 1
        elif coeff[i] == 0:
            continue
        else:
            result += str(coeff[i]) + 'x^' + str(j)
            j -= 1
    if coeff[-1] != 0:
        result = result[:len(result) - 3]
result += ' = 0'
print(result)
data.write(result)
data.close()

