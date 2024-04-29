# 3 Um determinado material radioativo perde metade de sua massa
# a cada 50 segundos. Dada a massa inicial, em gramas,
# fazer um programa em que calcule o tempo necessário para que essa massa
# se torne menor que 0,5 grama. O programa deve escrever a massa inicial,
# a massa final e o tempo calculado em segundos.

print(f'\n{"="*49}')
print(f'{" "*10}Calculadora de perda de Massa{" "*10}')
print(f'{"="*49}')

massa_inicial = float(input('\nInforme a massa inicial do material (em gramas): '))

segundos = 0
massa_final = massa_inicial

while True:

    massa_final /= 2
    segundos += 50

    if massa_final < 0.5:
        break

print(f'\nA massa inicial {massa_inicial:.2f}g do material levou {segundos} segundos '
      f'para chegar a massa de {massa_final:.2f}g!')