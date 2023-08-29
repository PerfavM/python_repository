#This is a Password Generator
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM
 
import random

print('                ---Generador de Contraseñas---')
print('                  ---Password Generator---\n')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = input('\n.:Amount of password to generate:.\n.:Cantidad de contraseña a generar:. ')
number = int(number)

length = input('\n.:Your password length:.\n.:Longitud de tu contraseña:. ')
length = int(length)

print('\n.:Here are your password:.\n.:Aqui tiene sus contraseñas:.\n')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)