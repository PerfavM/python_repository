#This is a file in English to guess the number.
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM

import time
import random

def guess(x):
  lives = 10
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_number:
      lives = lives - 1
      print(f'Sorry, guess again. Too low.') #U have {lives} op'
    elif guess > random_number:
      lives = lives - 1
      print(f'Sorry, guess again. Too high.') #U have {lives} op'
  print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
  """ if lives <= 0:
        print(f'Sorry, guess again, the number is {random_number}') """
  for caracter in guess:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
guess(10)

