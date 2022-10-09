# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
Range = [0, 1]
flag = True
for x in Range:
    for y in Range:
        for z in Range:
            A = not (x or y or z)
            B = not(x) and not(y) and not(z)
            print(x, y, z, A == B)
            if A != B:
                flag = False
if flag:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')