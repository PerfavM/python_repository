#This is a file in Spanish to guess the number.
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM

import random

def guess(x):
    lives = 10
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivina un número entre 1 y {x}: '))
        if guess < random_number:
            lives = lives - 1
            print(f'¡Lo siento!, demaciado bajo. ¡Intente de nuevo!.') #U have {lives} op
        elif guess > random_number:
            lives = lives - 1
            print(f'¡Lo siento!, demaciado alto. ¡Intente de nuevo!.')  #U have {lives} op
            
    print(f'¡Wow!, ¡Felicidades!, has adivinado que el numero es: {random_number}.!!')
    """ if lives <= 0:
        print(f'Sorry, guess again, the number is {random_number}') """
guess(10)
