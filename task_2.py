# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

A = not (x or y or z)
B = not x and not y and not z
result = A == B

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')