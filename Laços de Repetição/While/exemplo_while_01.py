from random import randint

while True:
    numero_01 = randint(1, 30)
    numero_02 = randint(1, 30)

    print(f'{numero_01} {numero_02}')

    if numero_01 == numero_02:
        break

