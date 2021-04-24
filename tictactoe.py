#tic tac toe

def start():
    global board
    board = [
        ['','',''],
        ['','',''],
        ['','','']
    ]

def print_board():
    print(' ---------')
    for row in board:
        print(' ',row[0],'|',row[1],'|',row[2])
        print(' --------')

def have_empty_space():
    for row in board:
        for space in row:
            if not space:
                return True
    return False

def set_space_state(spacexy,state):
    x = int(spacexy[0])-1
    y = int(spacexy[1])-1
    row = board[x]
    space = row[y]
    if not space:
        board[x][y] = state
        return True
    return False

def check_xy(xy):
    xy = str(xy)
    if len(xy) != 2:
        return False
    if int(xy[0]) > 3 or int(xy[0]) < 1 or int(xy[1]) > 3 or int(xy[1]) < 1:
        return False
    return True

def check_for_win():
    if board[0][0] == board[0][1] == board[0][2] != '':
        winner = board[0][0]
        print(f'{winner} won!')

    elif board[1][0] == board[1][1] == board[1][2] != '':
        winner = board[1][0]
        print(f'{winner} won!')

    elif board[2][0] == board[2][1] == board[2][2] != '':
        winner = board[2][0]
        print(f'{winner} won!')

    elif board[0][0] == board[1][0] == board[2][0] != '':
        winner = board[0][0]
        print(f'{winner} won!')

    elif board[0][1] == board[1][1] == board[2][1] != '':
        winner = board[0][1]
        print(f'{winner} won!')

    elif board[0][2] == board[1][2] == board[2][2] != '':
        winner = board[0][0]
        print(f'{winner} won!')
        
    elif board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        print(f'{winner} won!')
  
    elif board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        print(f'{winner} won!')

    else:
        return False
    
    return True


turn = 'o'
start()

while have_empty_space():
    print_board()
    print('\n')
    if turn == 'o':
        turn = 'x'
    else:
        turn = 'o'
    print(f'{turn}\'s Turn!')
    while True:
        xy = int(input('enter x and y: '))
        if check_xy(xy):
            if set_space_state(str(xy),turn):
                break
            print('This place is taken already')
            continue
        print('Error!')
        continue
    if check_for_win():
        break
print_board()
print('Game Over')
input()

