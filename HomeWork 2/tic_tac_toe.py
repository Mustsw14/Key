board = {'1,1':' ', '1,2':' ','1,3':' ','2,1':' ','2,2':' ','2,3':' ','3,1':' ','3,2':' ','3,3':' '}
player = 'X'
game_not_over = True

def print_board():
    print("    1 2 3")
    print(" 1 " +  board['1,1'] +" |"+ board['1,2']+ "|"+ board['1,3'])
    print("    _+_+_")
    print(" 2 " +  board['2,1'] +" |"+ board['2,2']+ "|"+ board['2,3'])
    print("    _+_+_")
    print(" 3 " +  board['3,1'] +" |"+ board['3,2']+ "|"+ board['3,3'])

def users_input():
    save_user_input = input(f"Enter {player} move (row,column no spaces)")
    if not check_correct_move(save_user_input):
        print("Invalid move, try again.")
        print_board()
        users_input()



def check_correct_move(save_user_input):
    global player
    if save_user_input in board.keys() and board[save_user_input]:
        board[save_user_input] = player
        return True
    else:
        return False



def check_if_game_over():
    global game_not_over
    global board
    if board['1,1'] == board['1,2'] == board['1,3'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")


    if board['2,1'] == board['2,2'] == board['2,3'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")


    if board['3,1'] == board['3,2'] == board['3,3'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")
        return True

    if board['1,1'] == board['1,2'] == board['1,3'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")
        return True

    if board['1,1'] == board['2,1'] == board['3,1'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")
        return True

    if board['1,2'] == board['2,2'] == board['3,2'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")
        return True

    if board['1,3'] == board['2,3'] == board['3,3'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")
        return True

    if board['1,1'] == board['2,2'] == board['3,3'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")
        return True

    if board['1,3'] == board['2,2'] == board['3,1'] != ' ':
        game_not_over = False
        print_board()
        print(f"{player} is the winner")
        return True

    value = ' '
    if value not in board.values():
        game_not_over = False
        print_board()
        print("It is a Tie")
        return True




def players_turn():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'


while game_not_over:
    print_board()
    users_input()
    if check_if_game_over() == True:
        break
    players_turn()
