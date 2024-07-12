import math

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(board, player):
    win_cond = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                (0, 4, 8), (2, 4, 6)]
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_cond)

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    human = 'X'
    ai = 'O'
    
    while True:
        print_board(board)
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = human
        
        if check_winner(board, human):
            print_board(board)
            print("You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        print("AI is making a move...")
        ai_move = best_move(board)
        board[ai_move] = ai
        
        if check_winner(board, ai):
            print_board(board)
            print("AI wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

# Run the game
tic_tac_toe()
