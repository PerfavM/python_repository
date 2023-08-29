#This is a file in Spanish to guess the number.
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
        feedback = input(f'¿Es {guess} demasiado alto (A), demasiado bajo (B), o es ese el numero (C)??').lower
        if feedback == 'a':
            high = guess -1
        elif feedback == 'b':
            low = guess + 1
    print(f'¡Wow!, ¡la computadora acaba de adivinar que tu numero es: {guess}.!')
    
computerGuess(10)