#This is a Calculate Example
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM

num1 = float(input("    Type the first number\n     Digite un numero: "))
num2 = float(input("    Type the second number\n    Digite otro numero: "))

operacion = input("Que operacion quiere utilizar??")

if operacion =='S':
    suma = num1 + num2
    print(f"\n  Result is\n  El Resultado es: {suma}" )
elif operacion =='R':
    resta = num1 - num2
    print(f"\n\n  Result is\n  El Resultado es: {resta}")
elif operacion =='M':
    multi = num1 * num2
    print(f"\n\n  Result is\n  El Resultado es: {multi}")
elif operacion =='D':
    div = num1 / num2
    print(f"\n\n  Result is\n  El Resultado es: {div:2f}")
else:
    print(f"\n  Please select a operacion    \nPorfavor selecione una operacion.")