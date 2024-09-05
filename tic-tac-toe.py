#Функция, которая рисует игровое поле 3х3
def drawing_board(board):
    #Запускаем цикл, который проходит по всем 3 строкам доски
    for i in range(3):
        #Метод join для объединения в 1 строку
        print(' | '.join(board[i]))
        print('---------')
#Тест функции
board = [[' ' for i in range(3)] for j in range(3)]
drawing_board(board)

#Функция, которая позволяет делать ход
def ask_and_make_move(player, board):
