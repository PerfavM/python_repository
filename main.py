import time
#import tkinter
#import pandas
#import django

print('''  #These are my ways to contact me.
  #Email: contactme@pfm-cv.me
  #Personal Email: moises.per.fav@gmail.com
  #Linkedin: https://www.linkedin.com/in/perez-favela-moises/
  #Portfolio Web: https://pfm-cv.me
  #GitHub: https://github.com/PerfavM\n''')
text = '  This file is a menu where all portfolio projects are listed as connected modules.\n  Este archivo es un menu donde vienen todos los proyectos del portafolio conectados como modulos\n \n  "Pleases select the language // Por favor selecione el idioma"\n'

for caracter in text:
  print(caracter, end='', flush=True)
  time.sleep(0.05)

print('''\n  1.English Languaje.
  2.Idioma Español.\n''')
lan = int(input(' '))

#languaje English
if lan == 1:
  text = '\n  This is the menu of the projects in English, please select the corresponding number.\n'
  for caracter in text:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
  
  #Menu English
  menu = print('''\n  01.Calculate
  02.Guess the number(pc).
  03.Guess the number(user).
  04.Rock, Papper, Scissers.
  05.Hangman.
  06.Countdown Timer.
  07.Password Generator.
  08.QR Code Generator.
  09.Tic-Tac-Toe.
  10.Binary Search
  11.Minesweeper
  12.Sudoku
  13.Bank\n''')
  """ 14.Pong
  15.Snake
  17.Connect four
  18.Tetris
  19.Binary Search
  20.Binary Search
  21.Binary Search
  22.Binary Search
  23.Binary Search
  24.Binary Search """
  text2 = int(input(' \n'))
  
  #while text2<0 and text2>25:
    #print(menu)
    #text2 = int(input(' '))
    
  #Madlibs
  if text2 == 1:
    from hello_world_python import calculate
    funcion = getattr(calculate, text2)
  #Guess the number(pc)
  elif text2 == 2:
    from hello_world_python import guess_the_number_en_pc
    funcion = getattr(guess_the_number_en_pc, text2)
  #Guess the number(user)
  elif text2 == 3:
    from hello_world_python import guess_the_number_en_user
    funcion = getattr(guess_the_number_en_user, text2)
  #Rock, Papper, Scissers.
  elif text2 == 4:
    from hello_world_python import rock_paper_scissors_en
    funcion = getattr(rock_paper_scissors_en, text2)
  #Hangman.
  elif text2 == 5:
    from hello_world_python import hangman
    funcion = getattr(hangman, text2)
  #Countdown Timer.
  elif text2 == 6:
    from hello_world_python import countdown_timer
    funcion = getattr(countdown_timer, text2)
  #Password Generator.
  elif text2 == 7:
    from hello_world_python import password_generator
    funcion = getattr(password_generator, text2)
  #QR Codificator/Descodificator
  elif text2 == 8:
    from hello_world_python import qr_code_en
    funcion = getattr(qr_code_en, text2)
  #Tic-Tac-Toe.
  elif text2 == 9:
    text = '\n  Sorry, but there was an error, please reboot and select another number\n  Or can see the file, it is in the next rute: "hello_world_python \ tic_tac_toe_game"\n'
    for caracter in text:
      print(caracter, end='', flush=True)
      time.sleep(0.05)
  elif text2 == 13:
    from hello_world_python import bank
    funcion = getattr(bank, text2)
  else:
    text = '\n  At this moment, there are some projects to be added, please restart the program and select another number\n'
    for caracter in text:
      print(caracter, end='', flush=True)
      time.sleep(0.05)
      
#Idioma español
elif lan == 2:
  text = '\n  Este es el Menu de los proyectos en español, por favor, selecione el numero correspondiente.\n'
  for caracter in text:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
    
  #Menu Español
  menu = print('''\n  01.Calculadora
  02.Adivina el numero(pc).
  03.Adivina el numero(user).
  04.Piedra, Papel, Tijeras.
  05.Ahorcado.
  06.Temporizador.
  07.Generador de contraseñas.
  08.Generador QR.
  09.Tic-Tac-Toe.
  10.Búsqueda binaria
  11.Buscaminas
  12.Sudoku
  13.Banco\n''')
  """ 13.Binary Search
  14.Binary Search
  15.Pong
  16.Snake
  17.Binary Search
  18.Tetris
  19.Binary Search
  20.Binary Search
  21.Binary Search
  22.Binary Search
  23.Binary Search
  24.Binary Search """
  text2 = int(input(' '))
  
  
  #Madlibs
  if text2 == 1:
    from hello_world_python import calculate
    funcion = getattr(calculate, text2)
  #Guess the number(pc)
  elif text2 == 2:
    from hello_world_python import guess_the_number_es_pc
    funcion = getattr(guess_the_number_es_pc, text2)
  #Guess the number(user)
  elif text2 == 3:
    from hello_world_python import guess_the_number_es_user
    funcion = getattr(guess_the_number_es_user, text2)
  #Rock, Papper, Scissers.
  elif text2 == 4:
    from hello_world_python import piedra_papel_tijeras_es
    funcion = getattr(piedra_papel_tijeras_es, text2)
  #Hangman.
  elif text2 == 5:
    from hello_world_python import hangman
    funcion = getattr(hangman, text2)
  #Countdown Timer.
  elif text2 == 6:
    from hello_world_python import countdown_timer
    funcion = getattr(countdown_timer, text2)
  #Password Generator.
  elif text2 == 7: 
    from hello_world_python import password_generator
    funcion = getattr(password_generator, text2)
  #QR Codificator/Descodificator
  elif text2 == 8:
    from hello_world_python import qr_code_es
    funcion = getattr(qr_code_es, text2)
  #Tic-Tac-Toe.
  elif text2 == 9:
    text = '\n  Disculpe, pero hubo un error, por favor, reinicie y seleccione otro numero\n  O si gusta ver el archivo, esta en la siguiente ruta: "hello_world_python \ tic_tac_toe_game"\n'
    for caracter in text:
      print(caracter, end='', flush=True)
      time.sleep(0.05)
  elif text2 == 13:
    from hello_world_python import bank
    funcion = getattr(bank, text2)
  else:
    text = '\n  En este momento, faltan algunos proyectos por agregar, por favor reinicie el programa y selecione otro numero\n'
    for caracter in text:
      print(caracter, end='', flush=True)
      time.sleep(0.05)