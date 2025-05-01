# Sua tarefa é escrever um programa simples que finge jogar tic-tac-toe com o usuário. 

# Para tornar tudo mais fácil para você, decidimos simplificar o jogo. Aqui estão nossas suposições:
# o computador (ou seja, seu programa) deve jogar usando 'X's;
# o usuário (por exemplo, você) deve jogar usando 'O's;
# o primeiro movimento pertence ao computador - ele sempre coloca seu primeiro 'X' no meio do quadro;
# todos os quadrados são numerados linha por linha, começando com 1 (consulte a sessão de exemplo abaixo para referência)
# o usuário insere seu movimento inserindo o número do quadrado escolhido - o número deve ser válido, ou seja, deve ser um número # inteiro, deve ser maior que 0 e menor que 10, e não pode apontar para um campo que já está ocupada;
# o programa verifica se o jogo acabou - há quatro veredictos possíveis: o jogo deve continuar, o jogo termina com um empate, # # # você ganha ou o computador ganha;
# o computador responde seu movimento e a verificação é repetida;
# não implementem qualquer forma de inteligência artificial - uma escolha de campo aleatória feita pelo computador é boa o suficiente para o jogo.

from random import randrange

def display_board(board):
    """Exibe o tabuleiro do jogo."""
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    """Lê a jogada do usuário e atualiza o tabuleiro."""
    while True:
        try:
            move = int(input("Digite seu movimento: "))
            if move < 1 or move > 9:
                print("Número inválido! Digite um número entre 1 e 9.")
                continue
            row, col = (move - 1) // 3, (move - 1) % 3
            if board[row][col] in ['X', 'O']:
                print("Campo já ocupado! Escolha outro.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Entrada inválida! Digite um número.")

def make_list_of_free_fields(board):
    """Retorna uma lista dos campos livres."""
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))
    return free

def victory_for(board, sign):
    """Verifica se o jogador com o símbolo especificado ganhou."""
    # Verifica linhas
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True
    # Verifica colunas
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True
    # Verifica diagonais
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

def draw_move(board):
    """Realiza a jogada do computador."""
    free = make_list_of_free_fields(board)
    if len(free) > 0:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'

# Inicializa o tabuleiro
board = [[3 * row + col + 1 for col in range(3)] for row in range(3)]
board[1][1] = 'X'  # Computador sempre começa no centro
free_fields = make_list_of_free_fields(board)
human_turn = True  # Agora é a vez do jogador humano

# Loop principal do jogo
while len(free_fields) > 0:
    display_board(board)
    if human_turn:
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("Você ganhou!")
            break
    else:
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("O computador ganhou!")
            break
    human_turn = not human_turn
    free_fields = make_list_of_free_fields(board)
    # Verifica empate dentro do loop
    if len(free_fields) == 0:
        display_board(board)
        print("Empate!")
        break