# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

user_count = int(input("Количество игроков?: "))
users = []
for i in range(user_count):
    user_name = input(f"Введите имя пользователя {i+1} ")
    users.append(user_name)

count = 0
сandies = 2021
max_take = 28

while сandies > 0:
    step = int(input(f"{users[count]}, твой ход: "))
    while step > max_take:
        step = int(input(f'{users[count]}, Не больше 28 конфет! '))
    сandies -= step
    count += 1
    if count == len(users):
        count = 0
    print(f"Осталось конфет: {сandies}")
    if сandies <= 28:
        break
print(f'Победитель - {users[count]}! Поздравляю!')
