#This is a Countdown Timer
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM

import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        
    print('Timer Completed! / ¡Tiempo Completado!')
    
print('                 ..::Countdown Timer::.. \n                    ..::Contador::.. \n')
t = input('Enter the time in seconds / Introdusca el tiempo en segundos: ')

countdown(int(t))