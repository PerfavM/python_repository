#This is a file in English to guess the number.
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM

import random

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' ''' and low != high ''':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay. The computer guessed your number, {guess}, correctly!')
    
computerGuess(10)