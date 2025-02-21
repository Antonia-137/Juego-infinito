import random

num = random.randint(1,50)
print(num)
jugador = int(input('Ingrese un numero: '))
print('ganaste al primer intento')

while num != jugador:
    print('numero equivocado, ingrese un numero: ')
    player = int(input('ingrese o'))
    if num == jugador:
        print('adivinaste el numero')
        break