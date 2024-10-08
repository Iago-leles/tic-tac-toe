import random
import os

class TicTacToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print("")
        print("" + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("---------")
        print("" + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("---------")
        print("" + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    def reset(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
        self.done = ''

    def check_win_or_draw(self):
        dict_win = {}

        for i in ["X", "O"]:
            # horizontais
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]

            #verticais
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]

            #diagonais
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]
        
        if dict_win["X"]:
            self.done = "X"
            print("X venceu!")
            return
        
        elif dict_win["O"]:
            self.done = "O"
            print("O venceu!")
            return

        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != ' ':
                    c += 1

        if c == 9:
            self.done = 'd'
            print('Empate!')
            return

    def get_player_move(self):
        invalid_move = True

        while invalid_move:
            try:
                print("Digite a linha do seu próximo lance")
                x = int(input())

                print("Digite a coluna do seu próximo lance")
                y = int(input())
                
                if x > 2 or x < 0 or y > 2 or y < 0:
                    print('Movimento invalido')
                
                if self.board[x][y] != ' ':
                    print('Posição já preenchida')
                    continue
            except Exception as e:
                print(e)
                continue

            invalid_move= False
        self.board[x][y] = 'X'


    def make_move(self):
        list_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    list_moves.append((i, j))

        if len(list_moves) > 0:
            x, y = random.choice(list_moves)
            self.board[x][y] = 'O'

game = TicTacToe()

game.print_board()

next = 0

while next == 0:
    os.system('cls')
    game.print_board()

    while game.done == "":
        game.get_player_move()
        game.make_move()
        os.system('cls')
        game.print_board()
        game.check_win_or_draw()
    
    print('Digite 1 caso você queira sair ou qualquer outro número para jogar novamente')
    
    try: 
        next = int(input())

        if next == 1:
            break
        else: 
            game.reset()
            next = 0
    except:
        print('Comando inválido')
