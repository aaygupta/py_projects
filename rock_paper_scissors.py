import random, sys

wins = 0
losses = 0
ties = 0

print('Welcome to Rock Paper Scissors Game, lets begin: ')

while True:
    print('Score Board: ' + str(wins) + ' Wins ' + str(losses) + ' Losses ' + str(ties) + ' Ties')
    while True:
        print('Enter move: (r)ock, (p)aper, (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()
        elif (player_move == 'r' or player_move == 'p' or player_move == 's'):
            break
        else:
            print('Invalid move. Please enter r,p,s or q.')

    comp_move_no = random.randint(1,3)
    options = {
        1:'r',
        2:'p',
        3:'s'
    }
    comp_move = str(options[comp_move_no])

    naming = {
        'r':'Rock',
        'p':'Paper',
        's':'Scissors'
    }
    print('\n' + str(naming[player_move]) + ' Vs ' + str(naming[comp_move]))

    if player_move == comp_move:
        print('Its a tie!')
        ties += 1
    elif player_move == 'r' and comp_move == 's':
        print('You win!')
        wins += 1
    elif player_move == 'r' and comp_move == 'p':
        print('You lost!')
        losses += 1
    elif player_move == 'p' and comp_move == 'r':
        print('You win!')
        wins += 1
    elif player_move == 'p' and comp_move == 's':
        print('You lost!')
        losses += 1
    elif player_move == 's' and comp_move == 'p':
        print('You win!')
        wins += 1
    elif player_move == 's' and comp_move == 'r':
        print('You lost!')
        losses += 1

