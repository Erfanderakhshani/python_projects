import random

def play():
    player = input("Please enter 'r' for rock, 'p' for paper and 's' for scissors: ".lower())
    print(f"You choice {player}")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer choice {computer}")
    if player == computer:
        print("Tie")

    elif is_win(player, computer):
        print('You win')
    else:
        print('You lose')


def is_win(player, opponent):
    #r > s, s > p, p> r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())

