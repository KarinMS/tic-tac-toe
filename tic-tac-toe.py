# Импортируем библиотеку, для раскраски проей
from colorama import Fore, Back, Style
#Функция, которая рисует игровое поле 3х3
# Создайте функцию, которая рисует и раскрашивает поле
def draw_board(board):
    # Запустите цикл, который проходит по всем строкам доски
    for x in range(3):
        # Запустите цикл, который проходит по всем столбцам доски
        for y in range(3):
            if board[x][y] == " ":
                if y < len(board) - 1:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, end=' | ')
                else:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL)
            elif board[x][y] == "X":
                if y < len(board) - 1:
                    print(Fore.RED + 'X' + Style.RESET_ALL, end=' | ')
                else:
                    print(Fore.RED + 'X' + Style.RESET_ALL)
            elif board[x][y] == "O":
                if y < len(board) - 1:
                    print(Fore.BLUE + 'O'  + Style.RESET_ALL, end=' | ')
                else:
                    print(Fore.BLUE + 'O'  + Style.RESET_ALL)
        print("---------")

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

# Функция, которая отслеживает выйгрышный ход
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

# Функция, которая управляет игрой
def tic_tac_toe():
    while True:
        board = [[' ' for i in range(3)] for j in range(3)]
        player = "X"
        while True:
            # Нарисовать игровое поле
            draw_board(board)
            # Запросить ход
            ask_and_make_move(player, board)
            # Проверить выйграл ли игрок
            if check_win(player, board):
                print(f'{player} выйграл')
                break
            # Проверить есть ли пустые клетки
            tie_game = False
            for row in board:
                for cell in row:
                    if cell == " ":
                        tie_game = True
            # Если произошла ничья то завершаем цикл
            if not tie_game:
                print("Ничья")
                break
            # Отдаем ход второму игроку (Тернарный оператор) (Результат - условие - иначе)
            player = "O" if player == "X" else "X"
            # Спросить не хотят ли сыграть снова
        restart = input("Хотите сыграть еще раз? (y/n) ")
        if restart.lower() != "y":
            break

tic_tac_toe()