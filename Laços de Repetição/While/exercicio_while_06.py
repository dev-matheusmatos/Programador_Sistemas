# 6 Escrever um algoritmo que leia uma quantidade desconhecida
# de números e conte quantos deles estão nos seguintes intervalos:
# [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deve terminar quando for lido um número negativo.

intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:

    numero = int(input('Informe um número: '))

    if numero >= 0:

        if numero < 26:

            intervalo_0_25 += 1

        elif numero < 51:

            intervalo_26_50 += 1

        elif numero < 76:

            intervalo_51_75 += 1

        elif numero < 101:

            intervalo_76_100 += 1

    else:
        break

print(f'\nA quantidade de números no intervalo [0-25] é de {intervalo_0_25}!')
print(f'A quantidade de números no intervalo [26-50] é de {intervalo_26_50}!')
print(f'A quantidade de números no intervalo [51-75] é de {intervalo_51_75}!')
print(f'A quantidade de números no intervalo [76-100] é de {intervalo_76_100}!')
