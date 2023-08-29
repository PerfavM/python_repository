#This is a Bank Example
#These are my ways to contact me.
#Email: contactme@pfm-cv.me
#Personal Email: moises.per.fav@gmail.com
#Linkedin: https://www.linkedin.com/in/perez-favela-moises/
#Portfolio Web: https://pfm-cv.me
#GitHub: https://github.com/PerfavM

print("\t.:Menu:.")
print('''\n  1.English Languaje.
  2.Idioma Español.\n''')
lan = int(input(' '))

if lan == 1:
  print("1. Deposit Money.")
  print("2. Withdraw Money.")
  print("3. Show balance.")
  print("4. Exit...")
  opcion = int(input("Please select a option:"))
  saldo = 1500
  
  if opcion ==1:
    ingreso = float(input("How much money do you want to deposit"))
    saldo += ingreso 
    print(f"Current balance: {saldo}")
  elif opcion ==2:
    retiro = float(input("How much money do you want to withdraw"))
    if retiro>saldo:
        print("Insufficient balance")
    else:
        saldo-=retiro
        print(f"Current balance: {saldo}")
  elif opcion ==3:
    print(f"Current balance: {saldo}")
  elif opcion==4:
    print("Thanks for your preference.")
  else:
    print("Error, Please select a option")

elif lan == 2:
  print("1. Ingresar dinero en la cuenta.")
  print("2. Retirar dinero de la cuenta.")
  print("3. Mostrar dinero disponible.")
  print("4. Salir...")
  opcion = int(input("Digite la opcion que quiera realizar:"))
  saldo = 1500
  

  if opcion ==1:
    ingreso = float(input("Cuanto dinero desea ingresar"))
    saldo += ingreso 
    print(f"Su saldo disponible es: {saldo}")
  elif opcion ==2:
    retiro = float(input("Cuanto dinero desea retirar"))
    if retiro>saldo:
        print("Saldo insuficiente")
    else:
        saldo-=retiro
        print(f"Su saldo disponible es: {saldo}")
  elif opcion ==3:
    print(f"Su saldo disponible es: {saldo}")
  elif opcion==4:
    print("Gracias por su preferencia.")
  else:
    print("Error, digite un numero que salga arriba")