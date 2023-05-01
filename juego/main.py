import random

opciones = ("piedra", "papel", "tijera")
from opciones import opciones
computer_win = 0
user_win = 0
rounds = 1

while True:
  print("*" * 10)
  print("ROUND", rounds)
  print("*" * 10)
  print("computer_win", computer_win)
  print("user_win", user_win)
  
  user_opcion = input("pidra, papel o tijera => ")
  user_opcion = user_opcion.lower()

  computer_opcion = random.choice(opciones) #elije de manera aleatoria
  print("User opcion=> ", user_opcion)
  print("Compute opcion=> ", computer_opcion)
  if not user_opcion in opciones: #si no la opcion del usuario esta dentra de la tupla de opciones le muestra una alerta
    print("la eleccion no es valida")
    continue
  
  if user_opcion == computer_opcion:
    print("empate")
  elif user_opcion == "piedra":
    if computer_opcion == "tijera":
      print("piedra gana a tijera")
      print("usuario gana")
      user_win += 1
    else:
      print("papel gana a piedra")
      print("computadora gana")
      computer_win +=1
  elif user_opcion == "papel":
    if computer_opcion == "piedra":
      print("papel gana a piedra")
      print("usuario gana")
      user_win += 1
    else:
      print("tijera gana a papel")
      print("computadora gana")
      computer_win += 1
  elif user_opcion == "tijera":
    if computer_opcion == "papel":
      print("tijera gana a papel")
      print("usuario gana")
      user_win += 1
    else:
      print("piedra gana a tijera")
      print("computadore gana")
      computer_win +=1
  if computer_win == 2:
      print("EL COMPUTADOR GANO")
      break
  if user_win == 2:
      print("EL USUARIO GANO")
      break
  rounds +=1