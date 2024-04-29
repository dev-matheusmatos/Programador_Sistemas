# Escreva uma função que calcule o mínimo múltiplo comum (MMC)
# de dois números inteiros.

def calcular_mmc(n1, n2):
    mmc = 0
    for i in range(n1 + 1):
        if (n1 * i) % n2 == 0:
            mmc = n1 * i
    if mmc == 0:
        mmc = n1 * n2
    return mmc


print(calcular_mmc(6, 10))