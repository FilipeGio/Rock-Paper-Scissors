from random import randint

rock = 'ROCK'
paper = 'PAPER'
scissor = 'SCISSOR'
option = [rock, paper, scissor]
computer = randint(0, 2)

print('Welcome to the Rock_Paper_Scissor game.')
select = int(input('Please player choose a number 1(Rock), 2(Paper), 3(Scissors): ')) - 1
if select <= 2:
    player = option[select]
    print(f'Player: {player} VS {option[computer]} :Computer')

if select == computer:
    print('That is a draw!')
elif select == 0:
    if computer == 1:
        print('Computer wins!')
    else:
        print('Player wins!')
elif select == 1:
    if computer == 0:
        print('Player wins!')
    else:
        print('Computer wins!')
elif select == 2:
    if computer == 0:
        print('Computer wins!')
    else:
        print('Player wins!')
else:
    print('You typed an invalid number you lose!')
