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
    x, y = input(f"{player}, введите координаты x и y (например: 1 1): ").split().strip()
    # Преобразовать координаты в целые числа
    x, y = int(x), int(y)
    # находится ли координата в пределах поля и свободно ли место
    if (0 < x < 2) and (0 < y < 2) and (board[x, y] == " "):
        # если свободно, записать значение игрока (Х или 0) в ячейку
        board[x, y] = player
    else:
        print("Это место уже занято. Попробуйте снова.")
        ask_and_make_move(player, board)

