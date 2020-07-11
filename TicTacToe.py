board = {
    'S1': ' ', 'S2': ' ', 'S3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' '
}

player = 1
total_moves = 0
end_check = 0


def check():
    #horizon(start)
    if board['S1'] == 'X' and board['S2'] == 'X' and board['S3'] == 'X':
        print('Player one won')
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print('Player one won')
        return 1
    if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
        print('Player one won')
        return 1
    #diogonal(start)
    if board['S1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
        print('Player one won')
        return 1
    #vertical(start)
    if board['S1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
        print('Player one won')
        return 1
    if board['S2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
        print('Player one won')
        return 1
    if board['S3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
        print('Player one won')
        return 1

    if board['S1'] == '0' and board['S2'] == '0' and board['S3'] == '0':
        print('Player two won')
        return 1
    if board['M1'] == '0' and board['M2'] == '0' and board['M3'] == '0':
        print('Player two won')
        return 1
    if board['D1'] == '0' and board['D2'] == '0' and board['D3'] == '0':
        print('Player two won')
        return 1
    # diogonal(start)
    if board['S1'] == '0' and board['M2'] == '0' and board['D3'] == '0':
        print('Player two won')
        return 1
    # vertical(start)
    if board['S1'] == '0' and board['M1'] == '0' and board['D1'] == '0':
        print('Player two won')
        return 1
    if board['S2'] == '0' and board['M2'] == '0' and board['D2'] == '0':
        print('Player two won')
        return 1
    if board['S3'] == '0' and board['M3'] == '0' and board['D3'] == '0':
        print('Player two won')
        return 1
    return 0


print('S1|S2|S3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('D1|D2|D3')
print('_____________________________________________________')

while True:
    print(board['S1'] + '|' + board['S2'] + '|' + board['S3'])
    print('-+-+-')
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('-+-+-')
    print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:
        if player == 1:
            p1_input = input('player one:')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print("Invalid input, please try again")
                continue
        else:
            p2_input = input('player two:')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = '0'
                player = 1
                break
            else:
                print("Invalid input, please try again")
                continue
    total_moves += 1
    print('_________________________________________')
    print()
