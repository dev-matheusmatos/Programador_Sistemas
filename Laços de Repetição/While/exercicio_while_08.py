# 8 Crie um programa que receba um número indeterminado de anos.
# Ao final, apresente quantos anos são pares, quantos são ímpares,
# quantos são bissextos, quantos são futuros (2024, 2025),
# e quantos são passado (2000, 2010)

qnt_anos = int(input('\nInforme a quantidade de anos: '))
pares = 0
impares = 0
bissextos = 0
anos_futuros = 0
anos_passados = 0
contador = 1

while True:

    ano = int(input(f'\nInforme o {contador}º ano: '))

    if ano % 2 == 0:
        pares += 1

    else:
        impares += 1

    if ano % 4 == 0 or (ano % 100 == 0 and ano % 400 == 0):
        bissextos += 1

    if ano >= 2024:
        anos_futuros += 1

    else:
        anos_passados += 1

    contador += 1

    if contador > qnt_anos:
        break

print(f'\nA quantidade de anos pares é de {pares}!')
print(f'A quantidade de anos ímpares é de {impares}!')
print(f'A quantidade de anos bissextos é de {bissextos}!')
print(f'A quantidade de anos futuros é de {anos_futuros}!')
print(f'A quantidade de anos passados é de {anos_passados}!')



