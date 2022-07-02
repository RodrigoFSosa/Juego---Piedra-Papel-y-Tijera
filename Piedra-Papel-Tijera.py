import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("¿Que escoges?")
mano=input("Escribe 0 para Piedra, 1 para Papel o 2 para Tijeras.\n")
#print(mano)
if mano == '0' or mano == '1' or mano == '2':
  if mano == '0':
    print(rock)
  elif mano == '1':
    print(paper)
  elif mano == '2':
    print(scissors)

  print("Elección de la computadora:")

  manoIA = str(random.randint(0,2))

  if manoIA == '0':
    print(rock)
  elif manoIA == '1':
    print(paper)
  elif manoIA == '2':
    print(scissors)

  ganador=2

  if mano == '0' and manoIA == '1':
    ganador = False
  elif mano == '0' and manoIA == '2':
    ganador = True
  elif mano == '1' and manoIA == '0':
    ganador = True
  elif mano == '1' and manoIA == '2':
    ganador = False
  elif mano == '2' and manoIA == '0':
    ganador = False
  elif mano == '2' and manoIA == '1':
    ganador = True
  else:
    print("Es un empate")

  if ganador == True:
    print("Ganaste!")
  elif ganador == False:
    print("Perdiste")

else:
  print("El tipo de entrada que ingresaste es inválido")

 