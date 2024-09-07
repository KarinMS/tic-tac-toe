#Функция, которая рисует игровое поле 3х3
def draw_board(board):
    #Запускаем цикл, который проходит по всем 3 строкам доски
    for i in range(3):
        #Метод join для объединения в 1 строку
        print(' | '.join(board[i]))
        print('---------')
#Тест функции
board = [[' ' for i in range(3)] for j in range(3)]
player = "X"
draw_board(board)


#Функция, которая позволяет делать ход
def ask_and_make_move(player, board):
    # Дать игроку возможность сделать ход
    x, y = ask_move(player, board)
    make_move(player, board, x, y)

#Функция, которая позволяет пользователю ввести координаты хода
def ask_move(player, board):
    # Дать игроку возможность сделать ход
    x, y = input(f"{player}, введите координаты x и y (например: 1 1): ").strip().split()
    # Преобразовать координаты в целые числа
    x, y = int(x), int(y)
    # находится ли координата в пределах поля и свободно ли место
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        # если свободно, вернуть ее координаты
        return x, y
    else:
        print("Клетка занята. Попробуйте снова.")
        return ask_move(player, board)

#Функция, которая непосредственно делает ход
def make_move(player, board, x, y):
    board[x][y] = player

#Функция, которая отслеживает выйгрышный ход
def check_win(player, board):
    for i in range(3):
        #Проверка по строкам
        if board[i] == [player, player, player]:
            return True
        # Проверка по столбцам
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    #проверка по диагонали

    if ((board[0][0] == player and board[1][1] == player and board[2][2] == player)
        or (board[2][0] == player and board[1][1] == player and board[0][2] == player)):
        return True
    return False

ask_and_make_move(player, board)