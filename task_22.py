# Создайте программу для игры в ""Крестики-нолики"".

users = []
for i in range(2):
    user_name = input(f"Введите имя {i+1} игрока: ")
    users.append(user_name)

game_board= [1,2,3,
             4,5,6,
             7,8,9]
 
win_combo = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
def print_game_board():
    print(game_board[0], game_board[1], game_board[2])
    print(game_board[3], game_board[4], game_board[5])
    print(game_board[6], game_board[7], game_board[8])

def step_game_board(step,symbol):
    ind = game_board.index(step)
    game_board[ind] = symbol
 
def get_result():
    win = ""
 
    for i in win_combo:
        if game_board[i[0]] == "X" and game_board[i[1]] == "X" and game_board[i[2]] == "X":
            win = users[0]
        if game_board[i[0]] == "O" and game_board[i[1]] == "O" and game_board[i[2]] == "O":
            win = users[1]                
    return win
 
game_over = False
player1 = True
 
while game_over == False:
 
    print_game_board()
 
    if player1 == True:
        symbol = "X"
        step = int(input(f"{users[0]}, ваш ход: "))
    else:
        symbol = "O"
        step = int(input(f"{users[1]}, ваш ход: "))
 
    step_game_board(step,symbol) 
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
      
print_game_board()
print("Победитель -", win)