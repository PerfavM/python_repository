#This is a game in English of rock, paper, scissors
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    if computer == 'r':
        computer = 'Rock'
    if computer == 'p':
        computer = 'Paper'
    if computer == 's':
        computer = 'scissors'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!, Computer choise ' + computer

    return 'You lost!, Computer choise ' + computer

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
