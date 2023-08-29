#This is a game in Spanish of rock, paper, scissors
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM

import random

def play():
    user = input("¿Cual es tu decision 'r' para Piedra, 'p' para Papel, 's' para Tijera\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return '¡Es un Empate!'
    
    if computer == 'r':
        computer = 'Piedra'
    if computer == 'p':
        computer = 'Papel'
    if computer == 's':
        computer = 'Tijera'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return '¡Ganaste!, La computadora eligio: ' + computer

    return '¡Perdiste!, La computadora eligio: ' + computer

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
